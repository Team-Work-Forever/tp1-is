import psycopg2
from helpers import SingletonMeta

class DbConnection(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self._connect()

    def _connect(self):
        self._connection = psycopg2.connect(user="is",
                                  password="is",
                                  host="is-db",
                                  port="5432",
                                  database="is")
        
    def get_cursor(self):
        return self._connection.cursor()
    
    def commit(self):
        self._connection.commit()
    
    def disconnect(self):
        self._connection.close()