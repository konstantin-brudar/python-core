# Обработка ошибок try/except

try:
    l = []
    l[42]
except Exception as e:
    print(e)

print("Exception is processed!")


try:
    a = 1 / 0
except Exception as e:
    print("division by zero is forbidden")


def several_catch():
    try:
        with open("file.log") as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except AssertionError as error:
        print(error)


try:
    print("Hello, Exceptions")
# Так писать нельзя! Нужно бить по рукам!
except:
    pass


# Генерация исключений через raise

def raise_exception():
    raise Exception("example of exception")


def check_str(string):
    if not isinstance(string, str):
        raise TypeError("not a string")

check_str("Hello")


def function_raising_exception():
    try:
        raise Exception("my raise!")
    except Exception as e:
        print(f"Логирование исключения: {e}")
        raise

try:
    function_raising_exception()
except Exception as e:
    print(f"Обработка исключения: {e}")


# Блоки else и finally в конструкции try/except

try:
    a = 42
except Exception as e:
    pass
else:
    print("Else block")


def foo():
    try:
        pass
    except:
        pass
    else:
        print("Please have mercy!")
        return None
    finally:
        print("Finish him!")

foo()


try:
    raise ValueError
except ValueError as e:
    print(1)
else:
    print(2)


# Инструкция assert

import sys

try:
    assert "windows" in sys.platform, "this code works only on windows"
except AssertionError:
    print("Do not use assert in production code")


# Типы исключений

try:
    raise ZeroDivisionError("деление на ноль")
    raise AssertionError("проверка внутри assert не выполнена")
    raise EOFError("в ходе считывания данных обнаружен EOF")
    raise ImportError("не получилось импортировать модуль")
    raise IndexError("обращение к элементу вне диапазона")
    raise KeyboardInterrupt("пользователь прервал процесс комбинацией клавиш")
    raise KeyError("обращение к отсутствующему ключу в контейнере")
    raise MemoryError("исчерпание свободной памяти")
    raise NameError("глобальное или локальное имя не найдено")
    raise RuntimeError("ошибка времени выполнения (в том числе использование не объявленной переменной)")
    raise SyntaxError("синтаксическая ошибка в коде программы")
    raise SystemError("ошибка работы интерпретатора")
    raise TypeError("прибавление числа к строке")
    raise ValueError("передача в функцию аргумента ожидаемого типа, но с неправильным значением")
except Exception as e:
    pass
