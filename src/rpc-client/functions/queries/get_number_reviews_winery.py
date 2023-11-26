import os
from functions import Handler

from xmlrpc.client import ServerProxy
from utils import MenuFactory

class GetNumberReviewsVinery(Handler):
    def __init__(self) -> None:
        super().__init__("Get Number of Reviews by Winery")

    def print_wine(self, wine):
        print(f"Winery - {wine[0]}")
        print(f"Reviews - {wine[1]}")

    def is_limit(self, limit):
        if len(limit) == 0:
            return False

        if not limit.isdigit():
            return True 
            
        return False

    def handle_function(self, server: ServerProxy):
        limit = 'limit'
        super().handle_function(server)

        files = server.get_all_persisted_files()
        files.append("all")
        files = files[::-1]

        index = MenuFactory().create_menu(title="Choose an file to search over or not", options=files)

        if index == -1:
            return

        while self.is_limit(limit):
            os.system("clear")
            limit = input("Provide the number of responses that you want to fetch (default = 10): ")

            if limit == '':
                limit = '10'
                break
        
        print("Quering...")

        if index == 0:
            wineries = server.get_number_reviews_winery('', int(limit))
        else:
            wineries = server.get_number_reviews_winery(files[index], int(limit))

        print("\nDone...", end="\n")
        for winery in wineries:
            self.print_wine(winery)
            print()

        print()
        input("Press enter")