from rpc_connection import RPConnection

from functions import GetStoragedFileHandler, UploadFileHandler

rpc_conn = RPConnection([
    UploadFileHandler(),
    GetStoragedFileHandler(),
]
).run_loop()