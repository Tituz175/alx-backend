#!/usr/bin/env python3
"""Module Documentation"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class documentation"""

    def __init__(self):
        """Constructor documentation"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.order:
                self.order.append(key)
            else:
                self.order.append(self.order.pop(self.order.index(key)))
            if len(self.order) > BaseCaching.MAX_ITEMS:
                removed_key = self.order.pop(-2)
                del self.cache_data[removed_key]
                print("DISCARD:{}".format(removed_key))

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data.keys():
            self.order.append(self.order.pop(self.order.index(key)))
            return self.cache_data[key]
        else:
            return None
