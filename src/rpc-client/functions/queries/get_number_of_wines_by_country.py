import os
from functions import Handler

from xmlrpc.client import ServerProxy
from utils import MenuFactory

class GetNumberOfWinesByCountry(Handler):
    def __init__(self) -> None:
        super().__init__("Get Number of Wines by Country")

    def print_response(self, response):
        print(f"Country - {response[0]}")
        print(f"Quantity of Wines - {response[1]}")

    def handle_function(self, server: ServerProxy):
        super().handle_function(server)
        print("Quering...")
        qty_wines = server.get_country_wines()

        print("Done...\n", end="\n")
        for qty in qty_wines:
            self.print_response(qty)
            print()

        print()
        input("Press enter")