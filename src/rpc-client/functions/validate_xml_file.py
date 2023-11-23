import os
from functions import Handler

from xmlrpc.client import ServerProxy

class ValidateXMLFileHandler(Handler):
    def __init__(self) -> None:
        super().__init__("Upload and Validate an XML file")

    def handle_function(self, server: ServerProxy):
        super().handle_function(server)

        path = input("Provide the path for the xml file: ")

        if not path:
            path = 'src/rpc-client/vendor/dataset.xml'

        file_name = os.path.basename(path)
        print("Uploading file and validating...")

        with open(path, 'r') as file:
            binary_data = file.read()

        response = server.validate_xml_file(binary_data)

        print(response)
        input("Press enter")
