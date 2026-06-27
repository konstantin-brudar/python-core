# map()

numbers = [32, 51, 3]
for n in map(hex, numbers):
    print(n)


l1 = [-2, 3, 1]
l2 = [0, 5, 8]
l3 = [1, 2, 0]
for res in map(lambda a, b, c: a + b + c, l1, l2, l3):
    print(res)


lst = [45, 9, -1, 0, 9, 1024, -1]
s = set(map(lambda n: "s" + str(n), lst))
print(s)


squares1 = [n*n for n in range(0, 5)]
squares2 = list(map(lambda n : n*n, range(0, 5)))
print(squares1)
print(squares1 == squares2)


products = {"corn": 5.2, "noodle": 6.5, "mayonnaise": 1.0}
discounted = dict(map(
    lambda item: (item[0], round(float(item[1])*(100-3)/100, 2)),
    products.items()
))
print(discounted)


# filter()

passwords = ["*****", "**", "*******", "*"]
safe_passwords = list(filter(lambda p: len(p) >= 3, passwords))
print(safe_passwords)


products = {"corn": 5.2, "noodle": 6.5, "mayonnaise": 1.0}
expensive = dict(filter(
    lambda item: float(item[1]) > 4,
    products.items()
))
print(expensive)


temperatures = (5, 0, -1, 6)
print(tuple(filter(None, temperatures)))


keys = ['u', 'u', '', 'd', 'h', '', '', 'r']
valid_keys = set(filter(None, keys))
print(valid_keys)


velocities = {60, 65, 90, 100, 120, 20, 40}
res1 = [f"{v} km/h" for v in velocities if v > 60]
res2 = list(map(lambda v: f"{v} km/h", filter(lambda v: v > 60, velocities)))
print(res1)
print(res1 == res2)


# functools.reduce()

from functools import reduce

def f(prev, cur):
    return prev * cur

res = reduce(f, [1, 2, 3, 4])
print(res)


def get_total_clicks(stats):
    def get_clicks(acc, d):
        clicks = 0 if d["is_bot"] else d["clicks"]
        return acc + clicks

    return reduce(get_clicks, stats, 0)

page_stats = [
    {
        "is_bot": True,
        "clicks": 2,
    },
    {
        "is_bot": False,
        "clicks": 3,
    },
    {
        "is_bot": False,
        "clicks": 1,
    }
]

print(get_total_clicks([]))
print(get_total_clicks(page_stats))
