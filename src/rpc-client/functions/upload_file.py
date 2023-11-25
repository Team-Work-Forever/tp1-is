import os
import xmlrpc.client

from helpers import EnviromentLoader

from functions import Handler
from utils import encode_file, decode_file, store_file
from xmlrpc.client import ServerProxy

class UploadFileHandler(Handler):
    def __init__(self) -> None:
        super().__init__("Convert CSV to XML")
        self.MAIN_DIR = EnviromentLoader.get_var("MAIN_DIR")

    def handle_function(self, server: ServerProxy):
        super().handle_function(server)
        
        path = input(F"Provide the path for the csv file ({self.MAIN_DIR}/dataset.csv): ")

        if not path:
            path = f'{self.MAIN_DIR}/dataset.csv'

        file_name = os.path.basename(path)

        print("Converting to XML...")

        with open(path, 'rb') as file:
            binary_data = encode_file(file.read())
        
        try:
            result = server.upload_file_to_xml(file_name, binary_data)

            file_name = file_name.split('.csv')[0] + ".xml"

            store_file(file_name, decode_file(result))
            print(f"Creating file {file_name}")
        except xmlrpc.client.Fault as fault:
            print(fault.faultString)

        input("Press enter")
