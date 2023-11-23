import signal, sys
from rpc_connection import RPConnection

from functions import GetStoragedFileHandler, UploadFileHandler, RemoveRecordHandler, RunQuery

# def load_file(folder_path, file):
#     module_name = f"functions.{file}"
#     module = import_module(module_name)

#     # Assuming each module has a class with the same name as the module
#     class_name = file.capitalize()  # Assuming classes start with an uppercase letter
#     handler_class = getattr(module, class_name)

# def load_from_assembly(folder_path):
#     files = []
#     current_path = os.getcwd()
#     folder_path = os.path.join(current_path, folder_path)

#     all_files = os.listdir(folder_path)

#     for file in all_files:
#         if file.endswith('.py') and file != '__init__.py':
#             load_file(folder_path, file)

# load_from_assembly("src/rpc-client/functions")

def signal_handler(signum, frame):
        print("Thanks, for using our cli")
        sys.exit(0)

rpc = RPConnection([
    UploadFileHandler(),
    GetStoragedFileHandler(),
    RemoveRecordHandler(),
    RunQuery()
])

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGHUP, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

rpc.run_loop()