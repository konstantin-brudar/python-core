# Базовый класс object

print(f"base of bool: {bool.__bases__}")
print(f"base of int: {int.__bases__}")
print(f"base of object: {object.__bases__}")
print(f"issubclass(bool, object): {issubclass(bool, object)}")

print(f"base of list: {list.__bases__}")
print(f"issubclass(list, object): {issubclass(list, object)}")

lst = [1, 2, 3]
print(f"isinstance(lst, object): {isinstance(lst, object)}")

print(f"base of type: {type.__bases__}")
print(f"issubclass(type, object): {issubclass(type, object)}")


# Объектная модель

class Dummy:
    pass

x = Dummy()

print(f"id: {id(x)}")
print(f"type: {type(x)}")
