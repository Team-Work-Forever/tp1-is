import signal, sys

from helpers import EnviromentLoader
from rpc_connection import RPConnection

from functions import load_handlers_by_assembly

if len(sys.argv) > 1:
    enviroment = sys.argv[1]
else:
    enviroment = 'dev'

EnviromentLoader.load(enviroment)

def signal_handler(signum, frame):
        print("Thanks, for using our cli")
        sys.exit(0)

rpc = RPConnection(load_handlers_by_assembly())

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGHUP, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

rpc.run_loop()