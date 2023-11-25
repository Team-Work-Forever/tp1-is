import os

from functions import Handler
from utils import MenuFactory

from .get_best_rated_wines import GetBestRatedWines
from .get_country_regions import GetCountryRegions
from .get_most_expensive_wines import GetMostExpensiveWines
from .get_number_of_wines_by_country import GetNumberOfWinesByCountry

from xmlrpc.client import ServerProxy

class RunQuery(Handler):
    queries = [
        GetBestRatedWines(),
        GetCountryRegions(),
        GetMostExpensiveWines(),
        GetNumberOfWinesByCountry()
    ]

    def __init__(self) -> None:
        super().__init__("Run Queries")

        self.query_names = [query.title for query in self.queries]

    def handle_function(self, server: ServerProxy):
        os.system("clear")
        index = MenuFactory().create_menu(title="Choose an query to run", options=self.query_names)

        if index == -1:
            return

        self.queries[index].handle_function(server=server)