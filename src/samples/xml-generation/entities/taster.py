from helpers.xml_exporter import XmlExporter
from .entity import Entity

class Taster(Entity):

    def __init__(self, name: str):
        super().__init__()

        self._name = name

    def get_name(self):
        return self._name
    
    def to_xml(self, xmlConverter: XmlExporter):
        return xmlConverter.convertTaster(self)