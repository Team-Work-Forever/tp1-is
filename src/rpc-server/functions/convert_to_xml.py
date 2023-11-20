import psycopg2
import asyncio

from functions import Handler
from xml_generation import CSVtoXMLConverter
from data import DbConnection
from utils import encode_file, decode_file, store_file

class ConvertToXmlHandler(Handler):
    VENDOR_FOLDER = "src/rpc-server/vendor/"
    DATASET_PATH = "dataset.csv"
    UPLOADS_FOLDER = "src/rpc-server/uploads/"

    def __init__(self) -> None:
        self.db_access = DbConnection()

    def get_name(self):
        return "upload_file_to_xml"

    def handle(self, file_name: str, csv_file: str):
        decoded_file = decode_file(csv_file)

        try:
            store_file(self.UPLOADS_FOLDER + "work_file", decoded_file)
        except Exception as e:
            print(e)
            return self.send_error("Error converting to XML")

        try:
            converter = CSVtoXMLConverter(self.UPLOADS_FOLDER + "work_file")
            xml_result = asyncio.run(converter.to_xml_str())
        except Exception as e:
            print(e)
            return self.send_error("Error converting to XML")

        cursor = self.db_access.get_cursor()

        query = """
            INSERT INTO imported_documents 
            (file_name, xml)
            VALUES 
            (%(file_name)s, %(xml)s);
        """

        try:
            cursor.execute(query, {
                'file_name': file_name,
                'xml': xml_result
            })

        except psycopg2.errors.UniqueViolation as e:
            print(e)
            return self.send_error("Is not possible to store the same file")

        self.db_access.commit()
      
        return encode_file(xml_result)