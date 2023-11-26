import asyncio
import xml.etree.ElementTree as ET

from data import DbConnection

from multiprocessing import Process
from .nominatim import NominatimApi

class NominatimWorker(Process):
    NOMINATIM_API = NominatimApi()

    def __init__(self, countries, regions, root_el: ET, converter) -> None:
        super().__init__()
        NominatimWorker.CACHE_MAP = {}

        self._db_connection = DbConnection()
        self._countries = countries
        self._regions = regions
        self._root_el = root_el
        self._converter = converter
     
    @staticmethod
    def get_key(country, region):
        return '-'.join([country, region])

    @staticmethod
    def insert_region(country, region, point):
        key = NominatimWorker.get_key(country, region)

        if key not in NominatimWorker.CACHE_MAP:
            NominatimWorker.CACHE_MAP[key] = [point]
        else:
            NominatimWorker.CACHE_MAP[key].append(point)

    @staticmethod
    def get_region(country, region):
        key = NominatimWorker.get_key(country, region)

        if key in NominatimWorker.CACHE_MAP:
            NominatimWorker.CACHE_MAP[key]
        
        return None

    async def run_request(self):
        for country in self._countries.values():
            for region in self._regions.values():
                if country.get_id() == region.get_country_id():
                    point = NominatimWorker.get_region(country.get_name(), region.get_region())

                    if point is not None:
                       api_request = point
                    else:
                        api_request = await NominatimWorker.NOMINATIM_API.get_value(country.get_name(), region.get_region())
                        NominatimWorker.insert_region(country.get_name(), region.get_region(), api_request)

                    region_el = self._root_el.find(".//Region[@id='" + region.get_id() + "']")
                    region_el.set("lat", str(api_request[0]))
                    region_el.set("lon", str(api_request[1]))
                    
    def run(self) -> None:
        asyncio.run(self.run_request())
        result = self._converter.to_xml_str(self._root_el)
        cursor = self._db_connection.get_cursor()

        query = """
            UPDATE imported_documents SET
                xml = %(xml)s
            WHERE file_name = %(file_name)s;
        """

        try:
            cursor.execute(query, {
                'file_name': self._converter.file_name,
                'xml': result
            })

        except Exception as e:
            print(e)

        self._db_connection.commit()
        print("done...")