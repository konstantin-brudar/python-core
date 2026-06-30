# Геттеры

class User:
    def __init__(self, user_id, name, email):
        self._id = user_id
        self._name = name
        self._email = email

    @property
    def data(self):
        return f"User {self._id}: name={self._name}, email={self._email}"

u = User(147, "kotiko", "kotiko@gmail.com")
print(u.data)


class Product:
    def __init__(self, number, count_total, count_reserved):
        self.number = number
        self.count_total = count_total
        self.count_reserved = count_reserved

    @property
    def count_available(self):
        return self.count_total - self.count_reserved

scanner = Product("scanner_3492", 19, 3)
print(scanner.count_available)


# Сеттеры

class Query:
    def __init__(self, q):
        self.query = q

    @property
    def query(self):
        return self._q.lower()

    @query.setter
    def query(self, new_val):
        self._q = new_val.strip()

q = Query("   погода Саратов сегодня  ")
print(q.query)


# Делитеры

class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, val):
        if val > 90 or val < -90:
            raise ValueError("Invalid latitude")
        self._lat = val

    @lat.deleter
    def lat(self):
        self._lat = 0.0

    @property
    def lon(self):
        return self._lon

    @lon.setter
    def lon(self, val):
        if val > 180 or val < -180:
            raise ValueError("Invalid longitude")
        self._lon = val

    @lon.deleter
    def lon(self):
        self._lon = 0.0

try:
    pos = Coordinate(34.0, -1004.5)
except ValueError as e:
    print(f"{type(e).__name__}: {e}")


# Свойства и наследование

class Parent:
    @property
    def field(self):
        print("Parent field")

    @field.setter
    def field(self, val):
        print("Parent setter")

class Child(Parent):
    @property
    def field(self):
        print("Child field")

c = Child()
c.field

try:
    c.field = 1
except AttributeError as e:
    print(f"{type(e).__name__}: {e}")


# Использование свойств без декораторов

from math import pi

class Circle:
    def __init__(self, x, y, r):
        self.r = r
        self.x, self.y = x, y

    def _get_r(self):
        return self._r

    def _set_r(self, value):
        if value < 0:
            raise ValueError("Negative radius")
        self._r = value

    def _get_area(self):
        return pi * self.r * self.r

    def _get_circumference(self):
        return 2 * pi * self.r

    r = property(
        fget=_get_r,
        fset=_set_r,
        doc="Circle radius"
    )

    area = property(fget=_get_area)

    circumference = property(fget=_get_circumference)

c = Circle(5, 2.01, 6)
print(c.area)
print(c.circumference)
