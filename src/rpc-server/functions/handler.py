from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_name(self):
        pass

    def handle(**kargs):
        pass