# Создание диапазона (range)

start = 0
stop = 4
step = 1
range(start, stop, step)
range(start, stop)
range(stop)

print(list(range(1, 4, 1)))
print(list(range(3, 0, -1)))

r = range(2, 5)
s = r[1:3]
print(s)


# Диапазоны и циклы

for i in range(3):
    print(i)

for i in range(8, -1, -2):
    print(i)


# Операции над диапазонами

print(list(range(10, 15)))
print(tuple(range(10, 15)))

print(35 in range(1,60))

print(range(8, -1, -2)[1])

print(range(10)[1:2])

r1 = range(1, 4, 2)
r2 = range(1, 5, 2)
print(r1 == r2)
print(r1 != r2)
