# zip()

cities = ["Podolsk", "Tver", "Voronej"]
locations = [(55.43, 37.54), (56.85, 35.90)]
places = tuple(zip(cities, locations))
print(places)


def match(*iterables):
    non_empty = list(filter(None, iterables))
    return list(zip(*non_empty, strict=True))

print(match([1, 2, 3], [], [9, 2, 0]))


a = ["A", "B", "C"]
b = ["D", "E", "F"]
paired = list(zip(a, b)) # [("A", "D"), ("B", "E"), ("C", "F")]
a2, b2 = zip(*paired)
assert a == list(a2) and b == list(b2)


# itertools.zip_longest()

from itertools import zip_longest

short = range(3)
long = range(5)

pairs = list(zip_longest(short, long, fillvalue="X"))
print(pairs)


# itertools.chain()

from itertools import chain

for x in chain("ABC", "DEF"):
    print(x, end=" ")

print()


games_shop_stats_april = [{
    "title": "Tower defense",
    "avg_rating": 3.4
},
{
    "title": "Hack and Slash RPG",
    "avg_rating": 3.6
}]

games_shop_stats_june = [
{
    "title": "Hack and Slash RPG",
    "avg_rating": 3.7
},
{
    "title": "Roguelike",
    "avg_rating": 4.1
}]

def get_best_genres(*stats):
    return set(map(lambda d: d["title"].lower(),
        filter(lambda d: d["avg_rating"] > 3.5, chain(*stats))))

print(get_best_genres(games_shop_stats_april, games_shop_stats_june))
