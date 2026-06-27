# Классы-декораторы

class SquareResult:
    def __init__(self, func):
        # момент декорирования
        self.func = func

    def __call__(self, *args, **kwargs):
        # момент вызова
        result = self.func(*args, **kwargs)
        return result**2

@SquareResult
def multiply(a, b):
    return a * b

print(multiply(2, 3))


# Готовые декораторы

# @classmethod и @staticmethod делают метод методом класса или статическим методом

# @abstractmethod помечает метод как абстрактный

# @atexit.register исполняет переданную в декоратор функцию при завершении скрипта, например, если вызван sys.exit()

# @typing.final подсказывает статическому анализатору, что метод является финальным, то есть не должен быть переопределен в классах-наследниках

# @property делает так, чтобы работать с методом класса как с полем, а не как с вызываемым объектом

# @functools.lru_cache кэширует результаты выполнения функции
