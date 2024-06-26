#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines an LFU caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.usage_freq = {}
        self.usage_order = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.usage_freq[key] += 1
                self.usage_order[key] = self.usage_order.pop(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lfu_key = min(self.usage_freq, key=lambda k: (
                        self.usage_freq[k], self.usage_order[k]
                        ))
                    del self.cache_data[lfu_key]
                    del self.usage_freq[lfu_key]
                    del self.usage_order[lfu_key]
                    print(f"DISCARD: {lfu_key}")

                self.cache_data[key] = item
                self.usage_freq[key] = 1
                self.usage_order[key] = len(self.usage_order)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.usage_freq[key] += 1
            self.usage_order[key] = self.usage_order.pop(key)
            return self.cache_data[key]
        return None

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")
