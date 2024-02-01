#!/usr/bin/env python3
"""Module Documentation"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Class documentation"""

    def __init__(self):
        """Constructor documentation"""
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data.keys():
                del self.order[key]
            elif len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
                removed_key, _ = self.order.popitem(last=False)
                del self.cache_data[removed_key]
                print("DISCARD:{}".format(removed_key))
            self.cache_data[key] = item
            self.order[key] = None

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data.keys():
            # Move the key to the end of the ordered dict to mark it as recently used
            del self.order[key]
            self.order[key] = None
            return self.cache_data[key]
        else:
            return None
