# Объекты, которые можно хранить в set, frozenset и dict

print(hash("some string"))
# print(hash(["some", "list"]))

print(hash((None, -2, False, 145.5, (2, 4, 8), "wednesday")))
# print(hash((list(), set(), dict())))


# Множества (set)

x = set()
print(x)
print(type(x))

web_frameworks = {"Django", "Flask", "FastAPI", "Flask"}
print(web_frameworks)

web_frameworks = set(["Django", "Flask", "FastAPI", "Flask"])
print(web_frameworks)

ml_libraries = set(("Pandas", "Pandas", "NumPy", "Keras", "TensorFlow"))
print(ml_libraries)

letters = set("AABBC")
print(letters)


# Операции над множествами

a = {1, 2, 3, 4, 5, 6, 7}
b = {5, 6, 7, 8, 9, 10}
c = {1, 3, 5, 7, 9, 11, 13, 15}
d = {1, 5, 7, 10, 15, 20}

res1 = a.intersection(b, c, d)
res2 = a & b & c & d
print(res1)
print(res1 == res2)

res1 = a.union(b, c, d)
res2 = a | b | c | d
print(res1)
print(res1 == res2)

res1 = a.difference(b, c, d)
res2 = a - b - c - d
print(res1)
print(res1 == res2)

res1 = a.symmetric_difference(b)
res2 = a ^ b
print(res1)
print(res1 == res2)


x = 1
a.add(x)
a.update(b)
a.remove(x)
a.discard(x)
a.pop()
a.clear()


a = {1, 3, 5, 7, 9}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(a.issubset(b))
print(a < b)

print(a < a)
print(a <= a)

print(a == a)

print(b.issuperset(a))
print(b > a)
print(b >= a)


# Неизменяемые множества

a = frozenset("abc")
b = set("bcd")
intersection = a & b
print(intersection)


hashable_types = ["int", "frozenset", "bool", "int"]
x = frozenset(hashable_types)
print(x)


print(hash(frozenset([1, 2, 3])))
# print(hash(frozenset([1, [], 3])))
