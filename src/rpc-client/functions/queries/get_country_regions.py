import os
from functions import Handler
from utils import MenuFactory

from xmlrpc.client import ServerProxy

class GetCountryRegions(Handler):
    def __init__(self) -> None:
        super().__init__("Get An Country Region")

    def print_region(self, file):
        print(f"Id - {file[0]}")
        print(f"Name - {file[1]}")
        print(f"Create On - {file[3]}")
        print(f"Updated On - {file[4]}")

    def handle_function(self, server: ServerProxy):
        os.system("clear")
        countries = server.get_countries()

        index = MenuFactory().create_menu(title="Choose an query to run", options=countries[:38])

        if index == -1:
            return

        regions = server.get_country_region(countries[index])

        for region in regions:
            print(region)

        print()
        input("Press enter")
