#!/usr/bin/env python3
"""Module Documentation"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class documentation"""

    def __init__(self):
        """Constructor documentation"""
        super().__init__()

    def put(self, key, item):
        """Function documentation"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Function documentation"""
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
