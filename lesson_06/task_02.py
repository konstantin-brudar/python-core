# Параметры и аргументы функции

def is_vowel(c):
    return c.lower() in ['a', 'e', 'i', 'o', 'u', 'y']


def count_vowels(s, n = None):
    if n is None:
        n = len(s)

    if n == 1:
        return is_vowel(s[n - 1])

    return count_vowels(s, n - 1) + is_vowel(s[n - 1])

print(count_vowels("Pascal!"))


# Позиционные и именованные аргументы

def f(a, b, c, d):
    pass

f(1, 2, c=3, d=4)

f(a=1, b=2, c=3, d=4)

f(d=4, c=3, a=1, b=2)


# Оператор return

import math

def get_circle_info(r):
    return math.pi * r * r, math.pi * 2.0 * r

area, circumference = get_circle_info(r=5.2)
print(area, circumference)


def no_return_function():
    print("Function does not return anything")

res = no_return_function()
print(res)
