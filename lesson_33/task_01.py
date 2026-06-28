# Аннотации для встроенных типов

x: bool = True
val: int = 2
a: float = 5.01
s: str = "ABC"

l: list[str] = ["A", "B"]
s: set[int] = {105, -9}
d: dict[int, bool] = {}

l: list = ["A", "B"]

def f(t: tuple[int, float, str]) -> None:
    ...

def f(t: tuple[int, ...]) -> None:
    ...

l: list[int | str]

x: list[int | None]


# Модуль typing

def some_check():
    return True

from typing import Optional
x: Optional[str] = "val" if some_check() else None


def some_magic():
    return 42

from typing import Any
obj: Any = some_magic()


from typing import Literal
ENDPOINTS = Literal["/search", "/suggest"]

def get_endpoint_rps(endpoint: ENDPOINTS) -> dict[ENDPOINTS, int]:
    return {endpoint: 3000}

print(get_endpoint_rps("/search"))


def validate_simple(data: Any) -> Literal[True]:
    return True


from typing import NoReturn
def f() -> NoReturn:
    while True:
        ...


# Модуль collections.abc

from collections.abc import Callable, Iterable, Iterator

def filter_vals(
    check_data: Callable[[int], bool], data: Iterable[int]
) -> Iterator[int]:
    return filter(check_data, data)

print(list(filter_vals(lambda x: x > 0, [-1, 3, -2, 8, 9])))


# Игнорирование типов в mypy

x = some_magic()  # type: ignore  # some_magic() won't return None here because ...


# Классы данных

class UserLocation:
    def __init__(self, lat, lon, ts, device_id):
        self.lat = lat
        self.lon = lon
        self.ts = ts
        self.device_id = device_id

loc = UserLocation(56.2, 34.0, 1725702413, "8d38823b97b66e9")
print(loc)


from dataclasses import dataclass

@dataclass
class UserLocation2:
    lat: float
    lon: float
    ts: int
    device_id: str

loc = UserLocation2(56.2, 34.0, 1725702413, "8d38823b97b66e9")
print(loc)


from dataclasses import dataclass

@dataclass
class Message:
    msg_id: int
    text: str = ""

print(Message(545))
