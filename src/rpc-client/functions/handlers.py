from abc import ABC

class Handler(ABC):

    def __init__(self, title: str) -> None:
        self.title = title

    def handle_function(self):
        pass