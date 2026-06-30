# Что такое метакласс

class Dummy:
    ...

d = Dummy()
print(type(d))
print(type(Dummy))
print(type(type))


class C:
    ...

x = C
print(type(x))
print(id(x))
print(id(C))


class C:
    ...

C.field = 8
print("field" in C.__dict__)


def factory(title):
    if title == "pancake":
        class Pancake:
            ...

        return Pancake

    if title == "brownie":
        class Brownie:
            ...

        return Brownie

    raise ValueError("Unexpected title")

x = factory("brownie")
print(type(x))
print(x.__name__)


# Встроенный метакласс type и динамическое создание классов

val = 104
print(type(val))
print(val.__class__)


class Dummy:
    ...

Dummy = type("Dummy", (), {})
print(len(Dummy.__bases__))


def show_summary(self):
    print(f"object type: {type(self)}")
    print(f"class parents: {type(self).__bases__}")

SimpleClass = type("SimpleClass", (), {"summary": show_summary})
obj = SimpleClass()
obj.summary()


# Кастомные метаклассы

class Dummy:
    ...

def new(cls):
    obj = object.__new__(cls)
    print(f"Creating object {obj}...")
    return obj

Dummy.__new__ = new

d = Dummy()


class Meta(type):
    def __new__(cls, name, bases, attrs):
        obj = super().__new__(cls, name, bases, attrs)
        print(f"Creating class {obj}...")
        return obj

class Dummy(metaclass=Meta):
    ...


class UpperAttrMeta(type):
    def __new__(cls, name, bases, attrs):
        uppercase_attrs = {}

        for k, v in attrs.items():
            method_name = k if k.startswith("_") else k.upper()
            uppercase_attrs[method_name] = v

        return super().__new__(cls, name, bases, uppercase_attrs)

class SimpleClass(metaclass=UpperAttrMeta):
    attr1 = "val1"
    attr2 = "val2"

print(hasattr(SimpleClass, "attr1"))
print(hasattr(SimpleClass, "ATTR1"))
