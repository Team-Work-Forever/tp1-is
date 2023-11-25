from functions import Handler

from xmlrpc.client import ServerProxy

class GetBestRatedWines(Handler):
    def __init__(self) -> None:
        super().__init__("Get 5 Best Rated Wines")

    def print_wines(self, file):
        print(f"Id - {file[0]}")
        print(f"Price - {file[1]}")
        print(f"Variaty - {file[2]}")
        print(f"Winery - {file[3]}")
        print(f"Designation - {file[4]}")

    def handle_function(self, server: ServerProxy):
        super().handle_function(server)
        wines = server.get_best_rated_wines()

        for wine in wines:
            self.print_wines(wine)
            print()

        input("Press enter")
