import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from helpers.xml_exporter import XmlExporter

from entities.country import Country
from entities.region import Region
from entities.taster import Taster
from entities.wine import Wine
from entities.review import Review

from csv_reader import CSVReader

class CSVtoXMLConverter:

    def __init__(self, path):
        self._reader = CSVReader(path)

    def read_countries(self):
        return self._reader.read_entities(
            attr="country",
            builder=lambda row: Country(row["country"])
        )
    
    def read_region(self, countries):
        return self._reader.read_entities(
            attr="region_1",
            builder=lambda row: Region(
                countries[row["country"]].get_id(),
                row["region_1"])
        )
    
    def read_wine(self, countries, regions):
        return self._reader.read_entities(
            attr="designation",
            builder=lambda row: Wine(
                row["price"], 
                row["designation"],
                countries[row["country"]].get_id(),
                regions[row["region_1"]].get_id(),
                row["variety"],
                row["winery"])
        )
    
    def read_taster(self):
        return self._reader.read_entities(
            attr="taster_name",
            builder=lambda row: Taster(
                row["taster_name"],
                row["taster_twitter_handle"])
        )
    
    def read_review(self, tasters, wines):

        return self._reader.read_entities(
            attr="points",
            builder=lambda row: 
                Review(
                    tasters[row["taster_name"]].get_id(),
                    wines[row["designation"]].get_id(),
                    row["points"],
                    row["description"])
        )

    def to_xml(self):
        xml_converter = XmlExporter()

        tasters = self.read_taster()
        countries = self.read_countries()
        regions = self.read_region(countries)

        wines = self.read_wine(countries, regions)
        reviews = self.read_review(tasters, wines)

        root_el = ET.Element("WineReviews")

        countries_el = ET.Element("Countries")

        for country in countries.values():
            country_parent = country.to_xml(xml_converter)
            countries_el.append(country_parent)
            
            for region in regions.values():
                if region.get_country_id() == country.get_id():
                    region_el = region.to_xml(xml_converter)
                    country_parent.append(region_el)

        wines_el = ET.Element("Wines")
        for wine in wines.values():
            wines_el.append(wine.to_xml(xml_converter))

        tasters_el = ET.Element("Tasters")
        for taster in tasters.values():
            tasters_el.append(taster.to_xml(xml_converter))

        reviews_el = ET.Element("Reviews")
        for review in reviews.values():
            review_parent = review.to_xml(xml_converter)
            reviews_el.append(review_parent)

        root_el.append(countries_el)
        root_el.append(wines_el)
        root_el.append(tasters_el)
        root_el.append(reviews_el)

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()

