from xml_generation.helpers.xml_exporter import XmlExporter
from .entity import Entity

class Region(Entity):

    def __init__(self, country_id, region, lat: float, lon: float):
        super().__init__("region")

        self._country_id = country_id
        self._region = region
        self._lat = lat
        self._lon = lon

    def get_country_id(self):
        return self._country_id
    
    def get_region(self):
        return self._region

    def get_lat(self):
        return self._lat

    def get_lon(self):
        return self._lon

    def set_lat(self, value: float):
        self._lat = value

    def set_lon(self, value: float):
        self._lon = value

    def to_xml(self, xmlConverter: XmlExporter):
        return xmlConverter.convertRegion(self)