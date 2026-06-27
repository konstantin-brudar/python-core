# Параметры декорируемых функций

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Args decorator!")
        result = func(*args, **kwargs)
        return result

    return wrapper

@decorator
def say(name, surname):
    return f"{name} {surname}"

print(say("Senior", "Junior"))


def str_checker(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                raise ValueError("all arguments must be strings")

        return func(*args, **kwargs)

    return wrapper

@str_checker
def concat(*words):
    return "~".join(words)

print(concat("A", "B", "C"))


# Метаданные функций

def decorator(func):
    def inner(*args, **kwargs):
        """decorator doc"""
        func(*args, **kwargs)

    return inner

@decorator
def f(*args):
    """f doc"""
    ...

print(f.__name__)
print(f.__doc__)


import functools

def decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        """decorator doc"""
        return func(*args, **kwargs)

    return inner

@decorator
def f(*args):
    """f doc"""
    ...

print(f.__name__)
print(f.__doc__)


# Фабрики декораторов

def factory(text):

    def decorator(func):

        def inner(*args, **kwargs):
            print(text)
            func()

        return inner

    return decorator

@factory("Fabric")
def f():
    print("f")

f()


import functools

def run_in_loop(n):

    def decorator(func):

        @functools.wraps(func)
        def wrapper():
            for i in range(n):
                func()

        return wrapper

    return decorator

@run_in_loop(4)
def f():
    """
    Test function
    """
    print("f")

f()

print(f.__name__)
print(f.__doc__)
