from data import DbConnection
from functions import Handler

class GetCountryRegions(Handler):
    def __init__(self) -> None:
        self.db_access = DbConnection()

    def get_name(self):
        return "get_country_region"

    def handle(self, country: str):
        result = []
        cursor = self.db_access.get_cursor()

        try:
            query = f"""
                select 
                    unnest(xpath('/WineReviews/Countries/Country[@name="{country}"]/Region/@region', xml))::text as Regions
                from imported_documents;
            """

            cursor.execute(query)

            result = cursor.fetchall()
        
        except Exception as e:
            print(e)
            return self.send_error("Is not possible to store the same file")

        return [value[0] for value in result]