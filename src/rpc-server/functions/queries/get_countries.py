from data import DbConnection
from functions import Handler

class GetCountries(Handler):
    def __init__(self) -> None:
        self.db_access = DbConnection()

    def get_name(self):
        return "get_countries"

    def handle(self):
        result = []
        cursor = self.db_access.get_cursor()

        try:
            query = f"""
                select
                    unnest(xpath('/WineReviews/Countries/Country[count(*) > 0]/@name', xml))::text as country
                from public.active_imported_documents
                where file_name = 'dataset.csv';
            """

            cursor.execute(query)

            result = cursor.fetchall()
        
        except Exception as e:
            print(e)
            return self.send_error("Is not possible to store the same file")

        return [value[0] for value in result]