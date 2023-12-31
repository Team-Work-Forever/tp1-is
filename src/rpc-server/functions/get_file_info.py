from functions import Handler
from data import DbConnection

class GetFileInfoHandler(Handler):
    def __init__(self) -> None:
        self.db_access = DbConnection()

    def get_name(self):
        return "get_file_info"

    def handle(self, file_name: str):
        cursor = self.db_access.get_cursor()
        cursor.execute(f"SELECT * FROM public.active_imported_documents where file_name = '{file_name}'")   

        get_file = cursor.fetchone()

        return (
            get_file[0],
            get_file[1],
            get_file[2],
            get_file[3],
            get_file[4]
        )