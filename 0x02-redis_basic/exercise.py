#!/usr/bin/env python3
"""
Redis with python
"""
import redis
import uuid
from typing import Union


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
