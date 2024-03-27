#!/usr/bin/env python3
"""
Redis with python
"""
import redis
import uuid
from typing import Union, Callable
import functools


class Cache():
    '''
    Class cache with instance of redis
    '''
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @functools.wraps
    def count_calls(method: Callable):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @functools.wraps
    def call_history(method: Callable):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            input_key = method.__qualname__ + ":inputs"
            output_key = method.__qualname__ + ":outputs"
            self._redis.rpush(input_key, str(args))
            output = method(self, *args, **kwargs)
            self._redis.rpush(output_key, str(output))
            return output
        return wrapper

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        function store that return a string
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None)\
            -> Union[str, bytes, int, float]:
        '''
        Takes in key and optional fn then
        converts data to desired format
        '''
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Transform a redis type variable to a str python type
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Transform a redis type variable to a str python type
        """
        return self.get(key, int)
