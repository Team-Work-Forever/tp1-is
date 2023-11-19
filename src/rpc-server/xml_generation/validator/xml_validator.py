import xml.etree.ElementTree as ET
from lxml import etree

class XMLValidator():
    XSD_SCHEMA = "src/rpc-server/vendor/dataset.xsd"

    def __init__(self, root):
        self._root = root
    
    def validate(self) -> bool:
        element = etree.fromstring(ET.tostring(self._root))
        schema = etree.XMLSchema(etree.parse(self.XSD_SCHEMA))

        return not schema.validate(element)