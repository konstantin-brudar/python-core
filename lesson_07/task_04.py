# Вариативные функции

def show_args(*args):
    print(f"Количество аргументов: {len(args)}")
    print(f"Аргументы: {args}")
    print(f"Тип args: {type(args)}")

show_args(1, 2, 3, "hello")


def show_kwargs(**kwargs):
    print(f"Количество именованных аргументов: {len(kwargs)}")
    print(f"Аргументы: {kwargs}")
    print(f"Тип kwargs: {type(kwargs)}")

show_kwargs(name="Alice", age=30, city="Moscow")


def show_all(*args, **kwargs):
    print(f"Позиционные аргументы: {args}")
    print(f"Именованные аргументы: {kwargs}")

show_all(1, 2, 3, name="Bob", age=25)
