import xml.etree.ElementTree as ET
from lxml import etree

class XMLValidator():
    XSD_SCHEMA = "./vendor/schema.xsd"

    def __init__(self, root):
        self._root = root
    
    def is_valid(self) -> bool:
        element = etree.fromstring(ET.tostring(self._root))
        schema = etree.XMLSchema(etree.parse(self.XSD_SCHEMA))

        return schema.validate(element)