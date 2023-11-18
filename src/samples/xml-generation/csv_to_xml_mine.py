import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from helpers.type_xml_configuration import TypeXmlConfiguration
from helpers.xml_configuration import XmlConfiguration

from config.country_xml_configuration import CountryXmlConfiguration
from config.taster_xml_configuration import TasterXmlConfiguration
from config.region_xml_configuration import RegionXmlConfiguration
from config.wine_xml_configuration import WineXmlConfiguration

from csv_reader import CSVReader


class CSVtoXMLMine:

    _configurations: [XmlConfiguration] = [
        CountryXmlConfiguration(),
        TasterXmlConfiguration(),
        RegionXmlConfiguration(),
    ]

    def __init__(self, path):
        self._reader = CSVReader(path)

    def to_xml(self):
        values = self._reader.read()
        print(values)
        root_el = ET.Element("WineReviews")

        for configuration in self._configurations:
            root_el.append(configuration.configure(TypeXmlConfiguration(values)))

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()

