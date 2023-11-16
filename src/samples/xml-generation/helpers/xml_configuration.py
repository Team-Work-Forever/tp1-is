from abc import ABC, abstractmethod
from .type_xml_configuration import TypeXmlConfiguration

class XmlConfiguration():

    def __init__(self) -> None:
        pass

    @abstractmethod
    def configure(self, builder: TypeXmlConfiguration) -> None:
        pass

__all__ = [TypeXmlConfiguration, XmlConfiguration]