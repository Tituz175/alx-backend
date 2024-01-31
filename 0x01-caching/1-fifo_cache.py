#!/usr/bin/env python3
"""Module Documentation"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class documentation"""

    def __init__(self):
        """Constructor docummentation"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            elif len(self.cache_data.keys()) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                removed_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(list(self.cache_data.keys())[0])
                print("DISCARD:{}".format(removed_key))
                self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
