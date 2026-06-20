# Ключевые слова global и nonlocal

path = "/tmp/"

def set_path():
    path = "/home/centos/"

set_path()
print(path)


path = "/tmp/"

def set_path():
    global path
    path = "/home/centos/"

set_path()
print(path)


def load_stats():
    global stats
    stats = 123

load_stats()
print(stats)


# Встроенные функции для работы с пространствами имен

x = 1

def f():
    a = "a"
    b = "b"
    print(locals())
    c = "c"

y = 2
f()


a = 1
b = 2

def f():
    x = 8

print(locals() is globals())
print(locals())


dir()


class A:
    def __init__(self):
        self.field1 = 1
        self.field2 = 2

obj = A()
print(vars(obj))
