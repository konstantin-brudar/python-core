# Объявление и вызов функции

def f():
    pass


def g(): pass


f()


# Docstring

def f():
    """This function does completely nothing"""
    pass


def fetch_records(table, ids):
    """Selects records from the table which correspond to ids.

    Args:
        table: name of the table in the database.
        ids: A sequence of integers representing the id of each record
            to fetch.

    Returns:
        A dict mapping id to the corresponding record in table.
    """
    pass


def print_sum(a, b):
    """ Выводит на экран сумму двух чисел.

        Args:
            a: Первое число.
            b: Второе число.

        Returns:
            Сумма a и b.
    """

    s = a + b
    print(s)

    return s


print_sum(3, 8)
