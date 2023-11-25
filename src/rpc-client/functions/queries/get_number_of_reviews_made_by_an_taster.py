from functions import Handler

from xmlrpc.client import ServerProxy

class GetNumberOfReviewsMadeByAnTaster(Handler):
    def __init__(self) -> None:
        super().__init__("Get Number of Reviews Made By an Taster")

    def print_response(self, response):
        print(f"Taster - {response[0]}")
        print(f"Quantity of Reviews - {response[1]}")

    def handle_function(self, server: ServerProxy):
        super().handle_function(server)
        print("Quering...")
        qty_reviews = server.get_number_of_reviews_made_by_an_taster()

        print("Done...\n", end="\n")
        for qty in qty_reviews:
            self.print_response(qty)
            print()

        print()
        input("Press enter")