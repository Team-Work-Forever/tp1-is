import importlib
import inspect
import os

from .handlers import Handler
from .get_stored_file import GetStoragedFileHandler
from .upload_file import UploadFileHandler
from .remove_record import RemoveRecordHandler

from .queries.run_query import RunQuery

def _get_module_classes():
    dirname_path = os.path.basename(os.path.dirname(__file__))

    module = importlib.import_module(dirname_path)
    classes = inspect.getmembers(module, inspect.isclass)

    return [obj[1] for obj in classes if obj[0] != 'Handler']

def load_handlers_by_assembly() -> [Handler]:
    class_instances = []
    classes = _get_module_classes()

    for cls in classes:
        try:
            instance = cls()
            class_instances.append(instance)
        except Exception as e:
            print(f"Error creating instance of {cls.__name__}: {e}")

    return class_instances

__all__ = [
    "GetStoragedFileHandler", 
    "UploadFileHandler", 
    "Handler", 
    "RemoveRecordHandler", 
    "RunQuery"
]