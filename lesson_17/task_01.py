# Наследование

class Parent:
    ...

class Child(Parent):
    ...


class Parent:
    def __init__(self, x):
        self.x = x
        print("Parent init")

    def f(self, val):
        print(f"Parent f({val})")
        return self.x * val

class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
        print("Child init")

    def f(self, val):
        print(f"Child f({val})")
        return self.x * self.y * val

parent = Parent(2)
res = parent.f(3)
print("Result:", res, "\n")

child = Child(2, 5)
res = child.f(3)
print("Result:", res)


# Задача 1

class Storage:
    def __init__(self, message_size_limit):
        self._message_size_limit = message_size_limit

    def save_message(self, message_id, message):
        print(f"Saving message {message_id}...")

    def get_message(self, message_id):
        print(f"Extracting message {message_id}...")

class InMemoryStorage(Storage):
    def __init__(self, message_size_limit, message_count_limit):
        super().__init__(message_size_limit)
        self._message_count_limit = message_count_limit
        self.messages = {}

    def save_message(self, message_id, message):
        super().save_message(message_id, message)

        if len(self.messages) > self._message_count_limit:
            raise Exception("Too many messages")

        if len(message) > self._message_size_limit:
            raise Exception("Message is too long")

        self.messages[message_id] = message

    def get_message(self, message_id):
        super().get_message(message_id)

        message = self.messages.get(message_id, None)

        return message

storage = InMemoryStorage(message_size_limit=10, message_count_limit=4)
storage.save_message(1, "First")
storage.save_message(2, "Second")
storage.save_message(3, "Third")
print(storage.get_message(2))
print(storage.get_message(10))


class A:
    def f(self, a, b):
        print("A", a, b)

class B(A):
    def f(self, a, b, c):
        print("B", a, b, c)

b = B()
b.f(1, 2, 3)


# Задача 2

from typing import Any

class EventHandler:
    def handle(self, event_type: str, payload: dict[str, Any]) -> bool:
        """Базовая обработка события. Возвращает True, если событие обработано."""
        print(f"[LOG] Handling {event_type} with payload: {payload}")
        return True

class ValidatingHandler(EventHandler):
    def handle(self, event_type: str, payload: dict[str, Any]) -> bool:
        if "timestamp" not in payload:
            raise ValueError("Missing timestamp")

        result = super().handle(event_type, payload)

        return result

handler = ValidatingHandler()
print(handler.handle("some event", {"timestamp":"01.02.2003"}))
