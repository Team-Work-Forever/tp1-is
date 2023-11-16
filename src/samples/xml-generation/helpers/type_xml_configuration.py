import xml.etree.ElementTree as ET

from .xml_exporter import XmlExporter

class TypeXmlConfiguration():

    _entities_list: [] = [ ] # { str, entidade }

    def __init__(self, values: { }) -> None:
        self._raw_values = values
        self._chosen_keys = []
        self._foreign_keys = {}
        self._key_values = {}

        self._configuration_el: ET.Element
        self._xml_exporter: XmlExporter = XmlExporter()
        self._current_entities = []

    def _get_key_entries(self, key: str):
        values = []

        for row in self._raw_values:
            value = row[key]

            if value not in values:
                values.append(value)

        return values
    
    def setHeaderName(self, headerName: str):
        self._configuration_el = ET.Element(headerName)

    def hasKeys(self, keys: []):
        for key in keys:
            values = self._get_key_entries(key)
            self._key_values[key] = values 
            
            self._chosen_keys.append(key)
    
    # def hasDependencies(self, dependencies: []):
    #     dependency = dependencies[0] # country

    #     for entry in self._entities_list:
    #         if entry[0] in self._get_key_entries(dependency):
    #             self._foreign_keys[dependency] = entry[1].get_id()

    #     print(self._foreign_keys)

    def isDependent(self):
        return len(self._foreign_keys) > 0

    def hasConvertion(self, labda):
        for values in zip(*(self._key_values[key] for key in self._chosen_keys)):
            data = {}

            for key, value in zip(self._chosen_keys, values):
                data[key] = value
            
            self._current_entities.append((values[0], labda(data) if not self.isDependent() else labda(data, self._foreign_keys)))
            self._entities_list.extend(self._current_entities)

    def build(self) -> ET.Element:
        for entry in self._current_entities:
            xml_value = entry[1].to_xml(self._xml_exporter)
            self._configuration_el.append(xml_value)

        return self._configuration_el