import xml.etree.ElementTree as ET
from lxml import etree

from helpers import EnviromentLoader

class XMLValidator():
    def __init__(self, root):
        self._root = root
        self.XSD_SCHEMA = EnviromentLoader.get_var("MAIN_DIR") + "/schema.xsd"
    
    def is_valid(self) -> bool:
        element = etree.fromstring(ET.tostring(self._root))
        schema = etree.XMLSchema(etree.parse(self.XSD_SCHEMA))

        return schema.validate(element)