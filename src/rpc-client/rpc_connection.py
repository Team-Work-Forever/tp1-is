from xmlrpc.client import ServerProxy

from helpers import EnviromentLoader

from utils import Console
from utils import MenuFactory
from functions import Handler

class RPConnection():

    def __init__(self, handlers: [Handler]) -> None:
        self.index = 0
        self.title_opts = []
        self.func_opts = []

        self.console = Console()

        for handler in handlers:
            self.title_opts.append(handler.title)
            self.func_opts.append(handler.handle_function)

    def run_loop(self):
        index = 0
        self.server = ServerProxy(f'http://{EnviromentLoader.get_var("RPC_SERVER_URL")}:9000')

        try:
            while True:
                index = MenuFactory().create_menu("RPC TP1", list(self.title_opts))

                if index == -1:
                    break

                self.func_opts[index](self.server)

        except Exception as e:
            self.console.clear()
            print(e)
        finally:
            self.console.reset()
            self.console.dispose()
        

        