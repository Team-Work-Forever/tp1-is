from rpc_connection import RPConnection

from functions import GetStoragedFileHandler, UploadFileHandler, RemoveRecordHandler

rpc_conn = RPConnection([
    UploadFileHandler(),
    GetStoragedFileHandler(),
    RemoveRecordHandler()
]
).run_loop()