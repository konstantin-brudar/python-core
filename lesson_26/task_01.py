# Позиционные и именованные аргументы

def f(x, *args, **kwargs):
    print(x)

    print(type(args))
    print(args)

    print(type(kwargs))
    print(kwargs)

f("x", 1, 2, 3, k1="a", k2="b")

lst = [1, 2, 3]
d = {"k1": "a", "k2": "b"}

f("x", *lst, **d)


def format(format_string, *params):
    ...

def analyze(**stats):
    ...


def analyze(*args, **kwargs):
    result = []
    for k, v in kwargs.items():
        if v in args:
            result.append(k)
    return result

print(analyze(1, 2, 3, k1=0, k2=3, k3=2, k4=1))


# Только именованные аргументы функций

def f(a1, a2, *, k1, k2):
    ...

f(1, 2, k1="val1", k2="val2")


# Только позиционные аргументы функций

def f(a, b, c=None, /):
    ...

def f(positional_only, /, positional_or_keyword, *, keyword_only):
    ...
