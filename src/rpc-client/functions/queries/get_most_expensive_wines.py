import os
from functions import Handler

from xmlrpc.client import ServerProxy
from utils import MenuFactory

class GetMostExpensiveWines(Handler):
    def __init__(self) -> None:
        super().__init__("Get Most Expensive Wines")

    def print_wine(self, wine):
        print(f"Id - {wine[0]}")
        print(f"Winery - {wine[1]}")
        print(f"Designation - {wine[2]}")
        print(f"Variaty - {wine[3]}")
        print(f"Price - {wine[4]} €")

    def is_limit(self, limit):
        if len(limit) == 0:
            return False

        if not limit.isdigit():
            return True 
            
        return False

    def handle_function(self, server: ServerProxy):
        super().handle_function(server)
        
        limit = 'a'

        files = server.get_all_persisted_files()
        files.append("all")
        files = files[::-1]

        index = MenuFactory().create_menu(title="Choose an file to search over or not", options=files)

        if index == -1:
            return

        while self.is_limit(limit):
            os.system("clear")
            limit = input("Provide the number of wines that you want to fetch (default = 10): ")
        
        print("Quering...")

        if index == 0:
            wines = server.get_the_most_expensive_wines('', int(limit))
        else:
            wines = server.get_the_most_expensive_wines(files[index], int(limit))

        print("\nDone...", end="\n")
        for wine in wines:
            self.print_wine(wine)
            print()

        print()
        input("Press enter")