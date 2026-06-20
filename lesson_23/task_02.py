# Бесконечные генераторы

from itertools import cycle

pool = cycle(["-", "\\", "|", "/"])

for i, elem in enumerate(pool):
    print(elem)
    if i > 5:
        break


def mycycle(lst):
    i = 0
    while True:
        yield lst[i]
        i = (i + 1) % len(lst)

pool = mycycle(["A", "B", "C"])

for i, elem in enumerate(pool):
    print(elem)
    if i > 5:
        break


# Встроенные функции для работы с генераторами

import sys

with open("file.txt") as f:
    print(sys.getsizeof(f))
    for l in f:
        print(l)


print(list(range(5)))
print(dict(enumerate(range(8))))


# Генератор с получаемым значением

def input_gen():
    while True:
        r = yield
        print(f"{r}")

c = input_gen()
c.send(None) # либо next(c)
c.send("Hi, input_gen")
next(c)
