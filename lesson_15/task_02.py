# Операции над словарем

cities = {}

cities["Tokyo"] = (35.6817, 139.7539)
cities["Cairo"] = (30.0505, 31.2464)

cairo_coordinates = cities["Cairo"]
print(f"Cairo is located here: {cairo_coordinates}")

n = len(cities)
print(f"We have {n} cities")


def add_user(name, email, users={"anonymous": None}):
    users[name] = email
    return users

add_user("admin", "admin@sj.ru")
print(len(add_user("test", "temp_mail@sj.ru")))


cities = {"Tokyo": (35.6817, 139.7539), "Cairo": (30.0505, 31.2464)}

print("Tokyo" in cities)
print("Palermo" in cities)

print(cities["Tokyo"])
# print(cities["Palermo"])


authors = {"Luciano Ramalho": "Fluent Python"}
authors["Luciano Ramalho"] = "Fluent Python. Clear, concise, and Effective programming"
authors["Jason Brownlee"] = "Python Asyncio Jump-Start"
print(authors)


f = lambda x: x % 10
d = dict()

for val in [15, 20, 30, 31]:
    k = f(val)
    d[k] = val

print(d)
print(len(d))


d = {3: "triangle", 4: "square", 6: "hexagon"}
del d[4]
print(d)


obj = [
    "sort",
    45,
    (16, 17),
    {
        1: 3,
        "k2": None,
        "k6": {
            "val": 1024
        }
    }
]
print(obj[3]["k6"]["val"])


d = {1: "One", "Two": 2, 3.5: "Three point five"}

for k in d:
    print(k, d[k])

for k, v in d.items():
    print(k, v)


def calc_visits(users):
    visited = set()
    result = {}

    for user in users:
        if user in visited:
            result[user] += 1
        else:
            visited.add(user)
            result[user] = 1

    return result

users = [6, 6, 4, 6]
print(calc_visits(users))


d = {1: "One", 2: "Two", 3: "Three"}
k = 1
default_val = 123

d_copy = d.copy()
d.clear()
d.pop(k, default_val)
d.get(k, default_val)
d.update([(10, "Ten"), (100, "hundred")])
d.setdefault(k, default_val)


def lexicon(text):
    d = {}

    for word in text.lower().split():
        d[word] = d.get(word, 0) + 1

    return d

lex = lexicon("A hash table uses a hash function to compute an index")

for k, v in lex.items():
    print(f"'{k}' occurs {v} times in text")

print(f"\nThere are {len(lex)} unique words in text")

del lex["a"]
del lex["an"]

print(f"There are {len(lex)} unique words in text excluding articles")


# Является ли dict упорядоченной коллекцией

d1 = {1: 1, 2: 2, 3: 3}
d2 = {2: 2, 3: 3, 1: 1}
print(d1 == d2)
