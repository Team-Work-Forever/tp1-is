import platform

from helpers import SingletonMeta

from .windows_menu import WindowsMenu
from .unix_menu import UnixMenu

class MenuFactory(metaclass=SingletonMeta):
    def create_menu(self, title: str, options: list[str]):
        if platform.system() == "Windows":
            return WindowsMenu(title=title, options=options).run()
        else:
            return UnixMenu(title=title, options=options).run()