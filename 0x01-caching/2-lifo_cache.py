#!/usr/bin/env python3
"""Module Documentation"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class documentation"""

    def __init__(self):
        """Constructor docummentation"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                removed_key, _ = self.cache_data.popitem()
                del self.cache_data[removed_key]
                print("DISCARD: {}". format(removed_key))

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
