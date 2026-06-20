# List comprehensions

numbers1 = []
for i in range(10):
    numbers1.append(i * i)

numbers2 = [i * i for i in range(10)]

print(numbers1 == numbers2)


dates = [i for i in range(1, 31)]
print(dates)


hexdates = [hex(i) for i in range(1, 31)]
print(hexdates)


three_divisable = [i for i in range(31) if i % 3 == 0]
print(three_divisable)


three_divisable = [i if i % 3 == 0 else -1 for i in range(10)]
print(three_divisable)


evens_and_odds = ["even" if i % 2 == 0 else "odd" for i in range(20)]
print(evens_and_odds)


l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
common = [i for i in l1 if i in l2]
print(common)


numbers = [[1, 2, 3, 4, 5], [6, 7]]

squares1 = []
for l in numbers:
   res = [n**2 for n in l if n%2 == 0]
   squares1.extend(res)

squares2 = [n**2 for l in numbers for n in l if n%2 == 0]
print(squares1 == squares2)


matrix1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
matrix2 = [[n for n in range(1,4)] for i in range(1,4)]
print(matrix1 == matrix2)


# set comprehension, dict comprehension

s = {i for i in [1, 2, 3, 1, 2, 4]}
print(s)


d = {i: i for i in range(10)}
print(d)


apis = [
    {
        "name": "search engine",
        "max_rps": 3000,
    },
    {
        "name": "analytics",
        "max_rps": 1100,
    },
    {
        "name": "crawler",
        "max_rps": 4000
    }
]
rps = [d["max_rps"] for d in apis]
print(rps)


apis = [
    {
        "name": "search engine",
        "max_rps": 3000,
    },
    {
        "name": "analytics",
        "max_rps": 1100,
    },
    {
        "name": "crawler",
        "max_rps": 3000
    }
]
plain = [val for d in apis for val in (d["name"], d["max_rps"])]
print(plain)
