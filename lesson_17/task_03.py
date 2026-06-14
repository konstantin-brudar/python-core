# Абстрактные классы

from abc import ABC, abstractmethod

class Cache(ABC):
    @abstractmethod
    def add(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass

class LRUCache(Cache):
    def __init__(self, max_items):
        self.max_items = max_items

    def add(self, key, value):
        print(f"Caching {key}...")

    def get(self, key):
        print("get() implementation")

lru_cache = LRUCache(1000)


class Navigation(ABC):
    @abstractmethod
    def build_route(self, start, finish):
        """
        Creates route between start and finish coordinates.
        Returns route object or None in case if the route couldn't be found.
        """
        ...

    @abstractmethod
    def get_maneuvers(self):
        """
        Returns list of maneuvers on the last route.
        """
        ...

class CarNavigation(Navigation):
    def build_route(self, start, finish):
        print("CarNavigation.build_route()")

    def get_maneuvers(self):
        print("CarNavigation.get_maneuvers()")

class TransitNavigation(Navigation):
    def build_route(self, start, finish):
        print("TransitNavigation.build_route()")

    def get_maneuvers(self):
        print("TransitNavigation.get_maneuvers()")

for nav in [CarNavigation(), TransitNavigation()]:
    nav.build_route(1, 2)
    nav.get_maneuvers()
