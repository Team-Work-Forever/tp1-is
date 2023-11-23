import asyncio

from functions import Handler
from xml_generation import CSVtoXMLConverter

from utils import store_file

class ValidateXMLFileHandler(Handler):
    UPLOADS_FOLDER = "src/rpc-server/uploads/"

    def get_name(self):
        return "validate_xml_file"

    def handle(self, xml_file):
        try:
            store_file(self.UPLOADS_FOLDER + "work_file", xml_file)
        except Exception as e:
            print(e)
            return self.send_error("Error converting to XML")

        try:
            CSVtoXMLConverter(self.UPLOADS_FOLDER + "work_file")
        except Exception as e:
            print(e)
            return self.send_error("Error converting to XML")

        return "This XML file is valid"