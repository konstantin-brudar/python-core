# Использование оператора моржа для заполнения коллекций

query = "Как варить макароны "
stats = (q := query.strip().lower(), len(q), q.split())
print(stats)


import math

def get_square_root(x):
    return (res := math.sqrt(x)), f"{res:.2f}"

print(get_square_root(10))


# Функция enumerate()

i = 1

for x in ["A", "B", "C"]:
    print(i, x)
    i += 1


for i, x in enumerate(["A", "B", "C"], start=1):
    print(i, x)


# Оператор is и неизменяемые типы

t1 = (1, 2)
t2 = (1, 2)
print(t1 is t2)


list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)
print(list1 is list2)
print(id(list1) == id(list2))
