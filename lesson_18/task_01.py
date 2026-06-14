# Как соотносятся классы и объекты

print(type(1))
print(type([1, 2, 3]))

print(type(int))
print(type(list))

print(type(type))


# Dunder-атрибуты (магические атрибуты)

class Example:
    def __init__(self):
        self.a = 10
        self.b = 5

print(Example())


class Example:
    def __init__(self):
        self.a = 10
        self.b = 5

    def __str__(self):
        return f"Example: a = {self.a}, b = {self.b}"

print(Example())


class Storage():
    def __init__(self, message_size_limit):
        self.message_size_limit = message_size_limit

    def __str__(self):
        return f"Storage with max {self.message_size_limit} characters"

    def __repr__(self):
        return f"Storage(message_size_limit={self.message_size_limit})"

storage = Storage(message_size_limit=5)

print(str(storage))
print(repr(storage))
