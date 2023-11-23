from functions import Handler

from xmlrpc.client import ServerProxy

class GetBestRatedWines(Handler):
    def __init__(self) -> None:
        super().__init__("Get 5 Best Rated Wines")

    def print_wines(self, file):
        print(f"Id - {file[0]}")
        print(f"Name - {file[1]}")
        print(f"Create On - {file[3]}")
        print(f"Updated On - {file[4]}")

    def handle_function(self, server: ServerProxy):
        super().handle_function(server)
        wines = server.get_best_rated_wines()

        for wine in wines:
            print(wine)

        input("Press enter")
