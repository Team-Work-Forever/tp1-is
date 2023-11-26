import xmlrpc.client
from functions import Handler

from helpers import EnviromentLoader

from xmlrpc.client import ServerProxy

class ValidateXMLFileHandler(Handler):
    def __init__(self) -> None:
        super().__init__("Upload and Validate an XML file")
        self.UPLOAD_DIR = EnviromentLoader.get_var("MAIN_DIR") + "/"

    def handle_function(self, server: ServerProxy):
        super().handle_function(server)

        path = input(f"Provide the path for the xml file ({self.UPLOAD_DIR}dataset.xml): ")

        if not path:
            path = self.UPLOAD_DIR + 'dataset.xml'

        try:
            with open(path, 'r') as file:
                binary_data = file.read()

            print("Uploading file and validating...")
            response = server.validate_xml_file(binary_data)
            print(response)
        except FileNotFoundError as e:
            print("File not found!")
        except xmlrpc.client.Fault as fault:
            print(fault.faultString)

        input("Press enter")
