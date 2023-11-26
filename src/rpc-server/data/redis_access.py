import redis

from helpers import EnviromentLoader, SingletonMeta

class RedisConnection(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self._connect()

    def _connect(self):
        self._connection = redis.StrictRedis(
            host=EnviromentLoader.get_var("REDIS_HOST"),
            port=EnviromentLoader.get_var("REDIS_PORT"),
            db=EnviromentLoader.get_var("REDIS_DB"))
        
    def get_value(self, key: str):
        value: bytes = self._connection.get(key)
        
        if value is not None:
            return value.decode('utf-8')
        
        return value

    def set_value(self, key: str, value: str):
        self._connection.set(key, value)
    
    def disconnect(self):
        self._connection.close()