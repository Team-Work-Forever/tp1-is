import os

from abc import ABC
from xmlrpc.client import ServerProxy

class Handler(ABC):

    def __init__(self, title: str) -> None:
        self.title = title

    def handle_function(self, server: ServerProxy):
        os.system("clear")