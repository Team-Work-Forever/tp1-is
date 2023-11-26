from utils import create_temp_file, delete_temp_file
from helpers import EnviromentLoader

from functions import Handler
from xml_generation import CSVtoXMLConverter

class ValidateXMLFileHandler(Handler):
    def __init__(self) -> None:
        self.UPLOADS_FOLDER = EnviromentLoader.get_var("MAIN_DIR") + "/"
        self.TEMP_FILE = self.UPLOADS_FOLDER + "temp"

    def get_name(self):
        return "validate_xml_file"

    def handle(self, xml_file):
        result = create_temp_file(self.TEMP_FILE, xml_file)

        if not result:
            return self.send_error("Error converting to XML")

        try:
            CSVtoXMLConverter(self.TEMP_FILE)
            delete_temp_file(self.TEMP_FILE)
        except Exception as e:
            print(e)
            return self.send_error("Error converting to XML")

        return "This XML file is valid"