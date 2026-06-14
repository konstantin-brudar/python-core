# Протоколы

from typing import Protocol

class Cache(Protocol):
    def add(self, key, value):
        pass

    def get(self, key):
        pass

class LRUCache:
    """
    Least recently used caching policy
    """
    def add(self, key, value):
        print(f"Caching {key} to LRU...")

    def get(self, key):
        print(f"Getting from LRU cache {key}...")

class MRUCache:
    """
    Most Recently Used caching policy
    """
    def add(self, key, value):
        print(f"Caching {key} to MRU...")

    def get(self, key):
        print(f"Getting from MRU cache {key}...")

def fill_cache(cache: Cache, source):
    for k, v in source.items():
        cache.add(k, v)

fill_cache(LRUCache(), {"key":"val"})
