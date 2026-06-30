# Мотивация

class D:
    def __init__(self):
        self.a = 1
        self.b = 2

    def f(self):
        ...

print("Instance attributes", D().__dict__)


# Что такое слоты

class S:
    __slots__ = ("a", "b")

    def __init__(self):
        self.a = 1
        self.b = 2

    def f(self):
        ...

print("Slots", S().__slots__)

try:
    print("Instance attributes", S().__dict__)
except AttributeError as e:
    print(f"{type(e).__name__}: {e}")

s = S()
try:
    s.c = 3
except AttributeError as e:
    print(f"{type(e).__name__}: {e}")


# Преимущества классов со слотами

from  pympler.asizeof import asizeof

class Message:
    def __init__(self, msg_id, text):
        self._id = msg_id
        self._text = text

class MessageSlots:
    __slots__ = ("_id", "_text")

    def __init__(self, msg_id, text):
        self._id = msg_id
        self._text = text

messages = [Message(x, str(x)) for x in range(1000)]
messages_slots = [MessageSlots(x, str(x)) for x in range(1000)]

print(f"asizeof(messages) = {asizeof(messages)}")
print(f"asizeof(messages_slots) = {asizeof(messages_slots)}")
