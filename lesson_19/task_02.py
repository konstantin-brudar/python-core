# Пользовательские типы исключений

class MyError(Exception):
    ...

def raise_my_error():
    raise MyError("this is my exception")

try:
    raise_my_error()
except Exception as e:
    print(e)


class UpperCaseError(Exception):
    pass

def upper_case_check(string):
    if string and not string[0].isupper():
        raise UpperCaseError(f"first letter of string '{string}' is not uppercase")

try:
    upper_case_check("Correct string")
    upper_case_check("wrong string")
except UpperCaseError as e:
    print(e)


# Цепочки исключений

def raise_from_error():
    try:
        result = 42 / 0
    except ZeroDivisionError as error:
        raise ValueError("operation not allowed") from error

def raise_from_none():
    try:
        result = 42 / 0
    except ZeroDivisionError as error:
        raise ValueError("operation not allowed") from None


# Группы исключений ExceptionGroup

def example_of_group_exception():
    try:
        raise ExceptionGroup(
            "several exceptions",
            [
                ValueError("invalid value"),
                TypeError("invalid type"),
                KeyError("missing key"),
            ],
        )
    except* ValueError as ver:
        print(ver.exceptions)
    except* TypeError as ter:
        print(ter.exceptions)
    except* KeyError as ker:
        print(ker.exceptions)


# Stack trace

import logging

try:
    raise ValueError
except ValueError as e:
    logging.exception(e)
print("Following program execution")
