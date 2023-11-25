import asyncio
import xml.etree.ElementTree as ET

from multiprocessing import Process
from .nominatim import NominatimApi

class NominatimWorker(Process):
    def __init__(self, countries, regions, root_el: ET) -> None:
        super().__init__()

        self._api = NominatimApi()
        self._countries = countries
        self._regions = regions
        self._root_el = root_el

    async def run_request(self):
        for country in self._countries.values():
            for region in self._regions.values():
                if country.get_id() == region.get_country_id():
                    api_request = await self._api.get_value(country.get_name(), region.get_region())
                    region_el = self._root_el.find(".//Region[@id='" + region.get_id() + "']")
                    region_el.set("lat", api_request[0])
                    region_el.set("lon", api_request[1])
                    print()
                    print(f"Country: {country.get_name()}, Region: {region.get_region()}")
                    print(f"lat: {api_request[0]}, lon: {api_request[1]}")

    def run(self) -> None:
        asyncio.run(self.run_request())
        print("done...")