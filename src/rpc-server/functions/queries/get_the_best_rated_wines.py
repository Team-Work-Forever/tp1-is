from functions import Handler
from data import DbConnection

class GetTheBestRatedWinesHandler(Handler):

    def __init__(self) -> None:
        self.dbAccess = DbConnection()

    def get_name(self):
        return "get_best_rated_wines"

    def handle(self):
        result = ''
        cursor = self.dbAccess.get_cursor()

        try:
            get_wines = f"""
                with wine_reviews as (
                    select
                    unnest(xpath('/WineReviews/Reviews/Review/@wine_id', xml))::text as wine_id,
                    (unnest(xpath('/WineReviews/Reviews/Review/@points', xml))::text::integer) as points
                from active_imported_documents
                ),
                wines as (
                    select
                    unnest(xpath('/WineReviews/Wines/Wine/@id', xml))::text as id,
                    (unnest(xpath('/WineReviews/Wines/Wine[@price > 0]/@price', xml))) as price,
                    unnest(xpath('/WineReviews/Wines/Wine/@variaty', xml)) as variaty,
                    unnest(xpath('/WineReviews/Wines/Wine/@winery', xml)) as winery,
                unnest(xpath('/WineReviews/Wines/Wine/@designation', xml)) as designation
                from active_imported_documents
                )
                select
                    w.*
                from wines w, wine_reviews wr
                where w.id = wr.wine_id
                order by wr.points desc
                limit 5;
            """

            cursor.execute(get_wines)
            result = cursor.fetchall()

        except Exception as e:
            print(e)
            return self.send_error("Some error has ocorred get the required information")

        return result