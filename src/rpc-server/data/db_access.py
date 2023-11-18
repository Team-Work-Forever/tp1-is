import psycopg2

class DbConnection():

    def __init__(self, connection_string) -> None:
        pass

    def connect(self):
        self._connection = psycopg2.connect(user="is",
                                  password="is",
                                  host="is-db",
                                  port="5432",
                                  database="is")
        
        return self._connection.cursor()
    
    def disconnect(self):
        self._connection.close()