import os

from functions import Handler

from xmlrpc.client import ServerProxy

class GetAveragePointsPerWine(Handler):
    def __init__(self) -> None:
        super().__init__("Get Average Points Per Wine")

    def print_response(self, response):
        print(f"Winery - {response[0]}")
        print(f"Average Points - {response[1]} pts")

    def is_limit(self, limit):
        if len(limit) == 0:
            return False

        if not limit.isdigit():
            return True 
            
        return False

    def handle_function(self, server: ServerProxy):
        limit = 'limit'
        order = 'order'
        super().handle_function(server)

        while self.is_limit(limit):
            os.system("clear")
            limit = input("Provide the number of wines that you want to fetch (default = 10): ")

            if limit == '':
                limit = '10'
                break

        while order != 'desc' and order != 'asc':
            os.system("clear")
            order = input("Provide the order (desc(defualt) | asc): ")

            if order == '':
                order = 'desc'
                break

        print("Quering...")
        qty_reviews = server.get_average_points_per_wine(int(limit), order)

        print("Done...\n", end="\n")
        for qty in qty_reviews:
            self.print_response(qty)
            print()

        print()
        input("Press enter")