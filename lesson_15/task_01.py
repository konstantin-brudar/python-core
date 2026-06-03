# Словарь (dict)
from lesson_11.task_01 import reversed_lst

empty1 = {}
empty2 = dict()
print(type(empty1), type(empty2))


users1 = {90278: "pasha", 136743: "slumbering.eoraptor"}
print(type(users1))
print(len(users1))

users2 = dict([
    (90278, "pasha"),
    (136743, "slumbering.eoraptor")
])
print(users1 == users2)


lst = ["or", "to", "an"]
d = dict(lst)
print(d)


products1 = dict([
    ("T3234FX", 12),
    ("T048Y11", 0),
    ("QW23302", 9)
])
print(products1)

products2 = dict(
    T3234FX=12,
    T048Y11=0,
    QW23302=9
)
print(products2)

print(products1 == products2)
