import psycopg2
from helpers import SingletonMeta

from helpers import EnviromentLoader

class DbConnection(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self._connect()

    def _connect(self):
        self._connection = psycopg2.connect(
            user=EnviromentLoader.get_var("DB_USER"),
            password=EnviromentLoader.get_var("DB_PASSWORD"),
            host=EnviromentLoader.get_var("DB_HOST"),
            port=EnviromentLoader.get_var("DB_PORT"),
            database=EnviromentLoader.get_var("DB_DATABASE"))
        
    def get_cursor(self):
        return self._connection.cursor()
    
    def commit(self):
        self._connection.commit()
    
    def rollback(self):
        self._connection.rollback()
    
    def disconnect(self):
        self._connection.close()