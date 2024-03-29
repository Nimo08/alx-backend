#!/usr/bin/env python3
"""
1-fifo_cache
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Inherits from BaseCaching and is a FIFO caching system"""

    def __init__(self):
        """Overload BaseCaching __init__"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        # If key already exists in cache, update value
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")
            self.cache_data[key] = item
            # Add key that comes after discarded first_key
            self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
