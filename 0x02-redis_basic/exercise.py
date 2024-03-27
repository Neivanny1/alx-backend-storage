#!/usr/bin/env python3
"""
Redis with python
"""
import redis
import uuid
from typing import Union, Callable


class Cache():
    '''
    Class cache with instance of redis
    '''
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

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
        self._redis.get(key)
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
