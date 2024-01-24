'''
this is the module
'''
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    '''
    this is a class
    '''
    def __init__(self):
        '''
        this is a function
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        this is a function
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int]]] = None) -> Union[str, int, bytes]:
        '''
        this is a function
        '''
        value = self._redis.get(key)
        if value is None:
            return value
        return value if fn is None else fn(value)

    def get_str(self, key: str) -> Optional[str]:
        '''
        this is a function
        '''
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        '''
        this is a function
        '''
        return self.get(key, fn=int)
