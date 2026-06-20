# Оператор моржа внутри comprehensions

def normalize(word):
    return word.strip().lower()

words = ["list ", " Comprehensions", ". "]
normalized = [n for w in words if len(n := normalize(w)) > 1]
print(normalized)


vals = [-100, 5, 19, 46, -99, 101]
cubes1 = [x**3 for x in vals if x**3 > 0]
cubes2 = [n for x in vals if (n := x**3) > 0]
print(cubes1 == cubes2)


# Генераторные выражения

import sys

g = (i * i for i in range(1000000))
print(sys.getsizeof(g))
print(sum(g))


# Comprehensions и кортежи

t = tuple(letter for letter in "generator expression")
print(t)


data = "data"

l = list(x for x in data)
print(l)

s = set(x for x in data)
print(s)

d = dict((x, x.upper()) for x in data)
print(d)
