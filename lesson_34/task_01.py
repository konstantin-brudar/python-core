# Что такое дескриптор

class MinMeasurement:
    def __get__(self, obj, objtype=None):
        return min(obj.measurements, default=0)

class Measurements:
    # Descriptor:
    min_measurement = MinMeasurement()

    def __init__(self, measurements):
        self.measurements = measurements

m1 = Measurements([2, -9, 4])
print(m1.min_measurement)

m2 = Measurements([100, 55, 50, 80])
print(m2.min_measurement)


import time
from datetime import datetime, timedelta

class Uptime:
    def __init__(self):
        self._ts_start = 0

    def __get__(self, obj, obj_type=None):
        now = time.time()
        sec = timedelta(seconds=int(now - self._ts_start))
        dt = datetime(1, 1, 1) + sec

        return (
            f"{dt.day-1} days, {dt.hour} hours, {dt.minute} minutes {dt.second} seconds"
        )

    def __set__(self, obj, ts_start):
        if ts_start <= 0:
            raise ValueError("Timestamp must be > 0")

        if ts_start > time.time():
            raise ValueError("Timestamp can't be in the future")

        self._ts_start = int(ts_start)

    def __delete__(self, obj):
        del self._ts_start

class Server:
    uptime = Uptime()

    def __init__(self, name, ts_start):
        self.name = name
        self.uptime = ts_start

server = Server("Sandbox", time.time())
time.sleep(2)
print(server.uptime)


# Виды дескрипторов

class X2:
    def __get__(self, obj, obj_type=None):
        return obj.x * 2

class Data:
    x2 = X2()

    def __init__(self, val):
        self.x2 = val

d = Data(5)
print(d.x2)


class Length:
    def __get__(self, obj, obj_type=None):
        return len(obj.lst)

    def __set__(self, obj, value):
        obj.lst = value

class Arr:
    l = Length()

    def __init__(self, data):
        self.l = data

a = Arr([1, 2, 3])
print(a.l)
