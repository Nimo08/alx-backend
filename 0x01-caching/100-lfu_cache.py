#!/usr/bin/env python3
"""
100-lfu_cache
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """Inherits from BaseCaching and is a LFU caching system"""

    def __init__(self):
        """Overloads BaseCaching __init__"""
        super().__init__()
        self.order = OrderedDict()
        self.frequency = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.order.move_to_end(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find minimum based on 2nd element i.e., frequency of item
            lfu_key = min(self.frequency.items(), key=lambda x: x[1])[0]
            del self.frequency[lfu_key]
            del self.cache_data[lfu_key]
            print(f"DISCARD: {lfu_key}")
        self.cache_data[key] = item
        self.frequency[key] = 1
        self.order[key] = None

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.order.move_to_end(key)
        return self.cache_data.get(key)
