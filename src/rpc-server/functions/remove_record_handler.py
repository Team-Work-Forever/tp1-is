import datetime
from functions import Handler
from data import DbConnection

from datetime import datetime

class RemoveRecordHandler(Handler):
    def __init__(self) -> None:
        self.db_access = DbConnection()

    def get_name(self):
        return "remove_record"

    def handle(self, file_name: str):
        cursor = self.db_access.get_cursor()

        query = """
            UPDATE imported_documents SET
                deleted_on = %(delete_on)s
            WHERE file_name = %(file_name)s;
        """

        try:
            cursor.execute(query, {
                'file_name': file_name,
                'delete_on': datetime.now()
            })

        except Exception as e:
            print(e)
            return self.send_error("Someting went wrong")

        self.db_access.commit()
        return "The record was removed from the database"