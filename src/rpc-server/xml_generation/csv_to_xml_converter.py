import asyncio
import time
import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from .helpers import XmlExporter
from .entities import Country, Wine, Region, Review, Taster

from .improve_csv_reader import BetterCSVReader
from .validator import XMLValidator

from services import NominatimApi

class CSVtoXMLConverter:

    def __init__(self, path):
        self._nominatimApi = NominatimApi()
        self._reader = BetterCSVReader(path)
        self._countries = None
        self._regions = None
        self._tasters = None
        self._wines = None
        self._reviews = None

    async def read_countries(self):
        if self._countries is None:
            self._countries = await self._reader.read_entities(
                attr="country",
                builder=lambda row: Country(row["country"])
            )

    def create_regions(self, row):
        value = row["region_1"]
        return value if value != "" else row["region_2"]

    def build_region(self, row, countries):
        country = countries[row["country"]]
        region = self.create_regions(row)

        return Region(country.get_id(), region, 0, 0)

    async def read_region(self, countries):
        if self._regions is None:
            self._regions = await self._reader.read_entities(
                attr="region_1",
                builder=lambda row: self.build_region(row, countries)
            )

    async def read_wine(self, countries, regions):
        if self._wines is None:
            self._wines = await self._reader.read_entities(
                attr="designation",
                builder=lambda row: Wine(
                    row["price"], 
                    row["designation"],
                    countries[row["country"]].get_id(),
                    regions[row["region_1"]].get_id(),
                    row["variety"],
                    row["winery"])
            )

    async def read_taster(self):
        if self._tasters is None:
            self._tasters = await self._reader.read_entities(
                attr="taster_name",
                builder=lambda row: Taster(
                    row["taster_name"],
                    row["taster_twitter_handle"])
            )

    async def read_review(self, tasters, wines):
        if self._reviews is None:
            self._reviews = await self._reader.read_entities(
                attr="points",
                builder=lambda row: Review(
                    tasters[row["taster_name"]].get_id(),
                    wines[row["designation"]].get_id(),
                    row["points"],
                    row["description"])
            )

    async def add_cord(self, country, region):
        try:
            response = await self._nominatimApi.get_value(country.get_name(), region.get_region())
            region.set_lat(response[0])
            region.set_lon(response[1])
        except Exception as e:
            print(e)

    async def get_locations(self):
        for country in self._countries.values():
            for region in self._regions.values():
                if country.get_id() == region.get_country_id():
                    time.sleep(4)
                    await self.add_cord(country, region)
        
    async def read_all_entities(self):
        await self.read_countries()
        await self.read_region(self._countries)

        await asyncio.gather(
            self.read_wine(self._countries, self._regions),
            self.read_taster(),
        )

        await self.read_review(self._tasters, self._wines)

    async def to_xml(self):
        xml_converter = XmlExporter()
        await self.read_all_entities()

        root_el = ET.Element("WineReviews")

        countries_el = ET.Element("Countries")

        for country in self._countries.values():
            country_parent = country.to_xml(xml_converter)
            countries_el.append(country_parent)
            
            for region in self._regions.values():
                if region.get_country_id() == country.get_id():
                    region_el = region.to_xml(xml_converter)
                    country_parent.append(region_el)

        wines_el = ET.Element("Wines")
        for wine in self._wines.values():
            wines_el.append(wine.to_xml(xml_converter))

        tasters_el = ET.Element("Tasters")
        for taster in self._tasters.values():
            tasters_el.append(taster.to_xml(xml_converter))

        reviews_el = ET.Element("Reviews")
        for review in self._reviews.values():
            review_parent = review.to_xml(xml_converter)
            reviews_el.append(review_parent)

        root_el.append(countries_el)
        root_el.append(wines_el)
        root_el.append(tasters_el)
        root_el.append(reviews_el)

        return root_el

    async def to_xml_str(self):
        root = await self.to_xml()
        validator = XMLValidator(root)

        if not validator.is_valid():
            raise Exception("Document XML is not valid")

        xml_str = ET.tostring(root, encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()
