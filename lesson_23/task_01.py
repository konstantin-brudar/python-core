# Итераторы и итерабельные объекты
from nis import cat

numbers = [1, 2, 3]

for n in numbers:
    print(n)

if 2 in numbers:
    print("found item")


class SeqIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item

        raise StopIteration

class SeqIterable:
    def __init__(self, sequence):
        self._sequence = sequence

    def __iter__(self):
        return SeqIterator(self._sequence)

for item in SeqIterable([1, 2, 3]):
    print(item)


vals = iter([1, 2, 3])
a = 2 in vals
b = 2 in vals
print(a)
print(b)


# Генераторы

def sequence_generator(sequence):
    for item in sequence:
        yield item

for number in sequence_generator([1, 2, 3]):
    print(number)


def f(items):
    for item in items:
        yield item

g = f('abcd')
print(list(g))

def f(items):
    yield from items

g = f('abcd')
print(list(g))


def even_sequence():
    i = 0
    while i <= 10:
        yield i
        i += 2

for item in even_sequence():
    print(item)


def strange_generator():
    print("before return")
    return
    print("after return")
    yield

g = strange_generator()
try:
    next(g)
except StopIteration:
    print("StopIteration")
