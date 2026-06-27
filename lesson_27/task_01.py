# Что такое декоратор

def outer():
    l = [1, 2, 3]

    def inner():
        return l

    return inner

obj = outer()
print(obj()) # calls inner()

outer = outer()
print(outer())


def outer(func):
    def wrapper(arg):
        arg += 2
        return func(arg)

    return wrapper


def increment(x):
    return x + 1

increment = outer(increment)
print(increment(4))


# Простой декоратор

from datetime import datetime

def log_func_start(func):
    def wrapper():
        dt = datetime.utcnow().isoformat(sep=" ", timespec="milliseconds")
        print(f"Function starts at {dt}")
        return func()

    return wrapper

def f():
    return "f() result"

f = log_func_start(f)

print(f())

@log_func_start
def f():
    return "f() result"

print(f())


import random
import string

def to_uppercase(func):
    def wrapper():
        return func().upper()

    return wrapper

@to_uppercase
def get_random_string():
    """
    Returns string consisting of 10 random ASCII letters
    """
    length = 10
    letters = string.ascii_lowercase

    return "".join(random.choice(letters) for i in range(length))

print(get_random_string())


import random
import time

def print_exec_time(func):
    def wrapper():
        start = time.perf_counter()
        func()
        finish = time.perf_counter()
        print(f"{finish - start:.2f} seconds")

    return wrapper

@print_exec_time
def slumber():
    time.sleep(random.randint(0, 3))

slumber()


# Цепочки декораторов

def brackets(func):
    def wrapper():
        return "[" + func() + "]"

    return wrapper

def parentheses(func):
    def wrapper():
        return "(" + func() + ")"

    return wrapper

@brackets
@parentheses
def f():
    return "baz"

print(f())
