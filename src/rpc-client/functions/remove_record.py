import os

from xmlrpc.client import ServerProxy

from utils import MenuFactory
from functions import Handler

class RemoveRecordHandler(Handler):
    def __init__(self) -> None:
        super().__init__("Remove Record")

    def handle_function(self, server: ServerProxy):
        os.system("clear")
        files = server.get_all_persisted_files()
        index = MenuFactory().create_menu(title="Choose an stored file", options=files)

        if index == -1:
            return

        result = server.remove_record(files[index])
        print(result)

        input("Press enter")
