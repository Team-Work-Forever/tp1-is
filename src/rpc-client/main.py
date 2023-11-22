from rpc_connection import RPConnection

from functions import GetStoragedFileHandler, UploadFileHandler, RemoveRecordHandler, RunQuery

rpc_conn = RPConnection([
    UploadFileHandler(),
    GetStoragedFileHandler(),
    RemoveRecordHandler(),
    RunQuery()
]
).run_loop()