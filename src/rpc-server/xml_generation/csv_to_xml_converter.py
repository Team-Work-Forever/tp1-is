import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from .helpers import XmlExporter
from .entities import Country, Wine, Region, Review, Taster

from .csv_reader import CSVReader
from .validator import XMLValidator

class CSVtoXMLConverter:

    def __init__(self, path):
        self._reader = CSVReader(path)

    def read_countries(self):
        return self._reader.read_entities(
            attr="country",
            builder=lambda row: Country(row["country"])
        )
    
    def create_regions(self, row):
        value = row["region_1"]

        if value == "":
            return row["region_2"]
        
        return row["region_1"]
    
    def read_region(self, countries):
        return self._reader.read_entities(
            attr="region_1",
            builder=lambda row: Region(
                countries[row["country"]].get_id(),
                self.create_regions(row))
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
        root = self.to_xml()
        validator = XMLValidator(root=root)

        if validator.validate():
            raise Exception("Invalid XML Format")

        xml_str = ET.tostring(root, encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)

        return dom.toprettyxml()

