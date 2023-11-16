import xml.etree.ElementTree as ET

class XMLValidator():
    _xml_file: str
    _schema_file: str
    
    def __init__(self, xml_file: str, schema_file: str):
        self._xml_file = xml_file
        self._schema_file = schema_file
    
    def load_file(self):
        tree = ET.parse(self._xml_file)
        root = tree.getroot()

        return root
    
    def load_schema(self):
        pass

    def validate(self) -> bool:
        root_tree = self.load_file()
        schema_tree = self.load_schema()

        return schema_tree.validate(root_tree)