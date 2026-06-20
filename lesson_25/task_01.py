# Распаковка

lst = ["a", "b", "c"]

a = lst[0]
b = lst[1]
c = lst[2]

a, b, c = lst

print(a, b, c)


s = "abc"
a, b, c = s
print(a, b, c)


# Множественное присваивание

a = 0
b = 1

swap = a
a = b
b = swap

print(a, b)


a = 0
b = 1

a, b = b, a

print(a, b)


lst = [0, 0]
i = 0

i, lst[i] = 1, 2

print(lst)


# Как устроена распаковка

a = 0
b = 1

tpl = a, b = b, a

print(tpl)
print(type(tpl))


a, b = b, a
a, b = (b, a)


# Варианты распаковки

d = {"a": 1, "b": 2}

k1, k2 = d
v1, v2 = d.values()
kv1, kv2 = d.items()

print(k1, k2)
print(v1, v2)
print(kv1, kv2)


a, b, c = range(100, 107, 3)
print(a, b, c)


clicks = [
    ("main page", 14),
    ("news page", 3)
]
for page_name, count in clicks:
    print(page_name, count)


databases = ["mongo", "clickhouse", "postgres"]
for i, db in enumerate(databases):
    print(i, db)


a, b, c = [i * i for i in range(1, 4)]
print(a, b, c)
