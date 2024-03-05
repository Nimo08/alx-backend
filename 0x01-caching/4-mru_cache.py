#!/usr/bin/env python3
"""
4-mru_cache.py
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """Inherits from BaseCaching and is a MRU caching system"""

    def __init__(self):
        """Overloads BaseCaching __init__"""
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.order[key]

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key, _ = self.order.popitem()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")
        self.cache_data[key] = item
        self.order[key] = None

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.order.move_to_end(key)
        return self.cache_data.get(key)
