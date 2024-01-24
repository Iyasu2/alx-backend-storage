'''
this is the module
'''
import redis
import uuid
from typing import Union


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
