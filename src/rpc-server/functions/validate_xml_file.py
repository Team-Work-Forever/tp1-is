from utils import create_temp_file, delete_temp_file
from helpers import EnviromentLoader

from functions import Handler
from xml_generation import XMLValidator

class ValidateXMLFileHandler(Handler):
    def __init__(self) -> None:
        self.UPLOADS_FOLDER = EnviromentLoader.get_var("MAIN_DIR") + "/"
        self.TEMP_FILE = self.UPLOADS_FOLDER + "temp"

    def get_name(self):
        return "validate_xml_file"

    def handle(self, xml_file):
        try:
            validator = XMLValidator()
            
            if not validator.is_valid_from_string(xml_file):
                raise Exception("Document is not valid!")
            
        except Exception as e:
            print(e)
            return self.send_error("Error converting to XML")

        return "This XML file is valid"