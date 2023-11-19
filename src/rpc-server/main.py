import signal, sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

from functions import ConvertToXmlHandler, GetAllPersistedFilesHandler, GetFileInfoHandler, RemoveRecordHandler
from data import DbConnection

dbAccess = DbConnection()

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

register_methods = [
    ConvertToXmlHandler(),
    GetAllPersistedFilesHandler(),
    GetFileInfoHandler(),
    RemoveRecordHandler()
]

with SimpleXMLRPCServer(('0.0.0.0', 9000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def signal_handler(signum, frame):
        print("received signal")
        server.server_close()

        # perform clean up, etc. here...

        print("exiting, gracefully")
        sys.exit(0)


    # signals
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    # register both functions
    for method in register_methods:
        server.register_function(method.handle, method.get_name())

    # start the server
    print("Starting the RPC Server...")
    server.serve_forever()

dbAccess.disconnect()