from helpers.xml_exporter import XmlExporter
from abc import abstractmethod

class Entity():
    def __init__(self) -> None:
        self._id = self._generate_id()

    def _generate_id(self):
        if not hasattr(self.__class__, '_id_counter'):
            self.__class__._id_counter = 0
        self.__class__._id_counter += 1
        return self.__class__._id_counter

    def get_id(self) -> int:
        return self._id
    
    @abstractmethod
    def to_xml(self, xmlConverter: XmlExporter):
        pass