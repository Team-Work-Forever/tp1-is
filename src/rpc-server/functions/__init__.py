import importlib
import inspect
import os

from .handler import Handler
from .convert_to_xml import ConvertToXmlHandler
from .get_all_persisted_files import GetAllPersistedFilesHandler
from .get_file_info import GetFileInfoHandler
from .remove_record_handler import RemoveRecordHandler
from .queries.get_the_best_rated_wines import GetTheBestRatedWinesHandler
from .queries.get_country_regions import GetCountryRegions
from .queries.get_countries import GetCountries
from .queries.get_the_most_expensive_wines import GetTheMostExpensiveWines

def get_module_classes():
    dirname_path = os.path.basename(os.path.dirname(__file__))

    module = importlib.import_module(dirname_path)
    classes = inspect.getmembers(module, inspect.isclass)

    return [obj[1] for obj in classes if obj[0] != 'Handler']

def load_handlers_by_assembly():
    class_instances = []
    classes = get_module_classes()

    for cls in classes:
        try:
            instance = cls()
            class_instances.append(instance)
        except Exception as e:
            print(f"Error creating instance of {cls.__name__}: {e}")

    return class_instances

__all__ = [
    "Handler", 
    "ConvertToXmlHandler", 
    "GetAllPersistedFilesHandler", 
    "GetFileInfoHandler", 
    "RemoveRecordHandler", 
    "GetTheBestRatedWinesHandler",
    "GetCountryRegions",
    "GetCountries",
    "GetTheMostExpensiveWines"
]