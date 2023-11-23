import psycopg2
from functions import Handler
from data import DbConnection

class GetTheBestRatedWinesHandler(Handler):

    def __init__(self) -> None:
        self.dbAccess = DbConnection()

    def get_name(self):
        return "get_best_rated_wines"

    def parse_ids_onto(self, ids):
        query = ''
        
        for wine_id in ids:
            query += '@id="' + wine_id[0] + '" or '

        return query[:-4]

    def handle(self):
        result = ''
        cursor = self.dbAccess.get_cursor()

        get_reviews = """
            SELECT
                unnest(xpath('/WineReviews/Reviews/Review/@wine_id', xml)) as wine_id,
                (unnest(xpath('/WineReviews/Reviews/Review/@points', xml))::text::integer) as points
            FROM public.active_imported_documents
            ORDER BY points desc
            limit 5
            ;
        """

        try:
            cursor.execute(get_reviews)
            wines_ids = cursor.fetchall()

            get_wines = f"""
            select
                    unnest(xpath('/WineReviews/Wines/Wine[{self.parse_ids_onto(wines_ids)}]', xml))::text as wine_id
                from public.active_imported_documents;
                ;      
            """

            cursor.execute(get_wines)
            result = cursor.fetchall()

        except psycopg2.errors.UniqueViolation as e:
            print(e)
            return self.send_error("Some error has ocorred get the required information")

        return result