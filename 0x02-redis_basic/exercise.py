#!/usr/bin/env python3
"""
Redis module
"""
import sys
from functools import wraps
from typing import Union, Optional, Callable, List
from uuid import uuid4

import redis

UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """
    A function
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        A function
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A function
    """
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ A function """
        self._redis.rpush(i, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(o, str(res))
        return res

    return wrapper


class Cache:
    """
    A class
    """

    def __init__(self):
        """
        A function
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: UnionOfTypes) -> str:
        """
        A function
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> UnionOfTypes:
        """
        A function
        """
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_int(self, data: bytes) -> int:
        """A function"""
        return int.from_bytes(data, sys.byteorder)

    def get_str(self, data: bytes) -> str:
        """A function"""
        return data.decode("utf-8")

    def replay(self, method: Callable) -> None:
        """
        A function
        """
        key = method.__qualname__
        i = "".join([key, ":inputs"])
        o = "".join([key, ":outputs"])

        inputs = self._redis.lrange(i, 0, -1)
        outputs = self._redis.lrange(o, 0, -1)

        print(f"{key} was called {len(inputs)} times:")

        for input_params, output_key in zip(inputs, outputs):
            input_args = eval(input_params.decode('utf-8'))
            output_data = self._redis.get(output_key.decode("utf-8"))
            print(f"{key}(*{input_args}) -> {output_data.decode('utf-8')}")
