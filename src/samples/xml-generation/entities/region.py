from helpers.xml_exporter import XmlExporter
from .entity import Entity

class Region(Entity):

    def __init__(self, country_id, region):
        super().__init__("region")

        self._country_id = country_id
        self._region = region

    def get_country_id(self):
        return self._country_id
    
    def get_region(self):
        return self._region
    
    def to_xml(self, xmlConverter: XmlExporter):
        return xmlConverter.convertRegion(self)