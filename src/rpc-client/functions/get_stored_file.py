from functions import Handler

from utils import store_file
from xmlrpc.client import ServerProxy
from utils.menu.menu_factory import MenuFactory

class GetStoragedFileHandler(Handler):
    def __init__(self) -> None:
        super().__init__("Get All Uploaded Files")

    def print_file(self, file):
        print(f"Id - {file[0]}")
        print(f"Name - {file[1]}")
        print(f"Create On - {file[3]}")
        print(f"Updated On - {file[4]}")

    def handle_function(self, server: ServerProxy):
        super().handle_function(server)

        files = server.get_all_persisted_files()
        index = MenuFactory().create_menu(title="Choose an stored file", options=files)

        if index == -1:
            return

        file_info = server.get_file_info(files[index])
        self.print_file(file_info)

        store_file(files[index].split('.csv')[0] + ".xml", file_info[2])

        input("Press enter")
