# Поиск элемента: if vs метод get()

d = {"one":1, "two":2, "three":3}
k = "one"

x = 1
if k in d:
    x = d[k]

x = d.get(k, 1)


# Обновление элемента: if vs класс defaultdict

d = {"one":[1], "two":[1, 2], "three":[3, 4, 5]}
k = "ten"

if k not in d:
    d[k] = []
d[k].append("some value")

from collections import defaultdict
d = defaultdict(list)
d[k].append("some value")


# Обновление элемента: if vs метод setdefault()

d = {"one":[1], "two":[1, 2], "three":[3, 4, 5]}
k = "ten"

if k not in d:
    d[k] = []
d[k].append("some value")

d.setdefault(k, []).append("some value")


# Циклы: обращение по ключу vs метод items()

d = {"one":1, "two":2, "three":3}

for k in d:
    print(k, d[k])

for k, v in d.items():
    print(k, v)


# Поиск по списку vs поиск по множеству

lst = [1, 2, 3, 5, 10]
x = 5

if x in lst:
    print(f"Found {x} in list!")

s = set(lst)
if x in s:
    print(f"Found {x} in set!")


# Циклы: len() + range() vs enumerate()

lst = ["a", "b", "c"]

for i in range(0, len(lst)):
    elem = lst[i]
    print(i, elem)

for i, elem in enumerate(lst):
    print(i, elem)


# List comprehensions vs generator expressions

words = ["apple", "banana", "cherry"]

comma_seperated_words = ','.join([word for word in words])

comma_seperated_words = ','.join(word for word in words)


# Как заглянуть внутрь собственного кода

import dis

dis.dis('(1, 2) is (1, 2)')

code = compile('(1, 2) is (1, 2)', '<string>', 'single')
print(code.co_consts)
