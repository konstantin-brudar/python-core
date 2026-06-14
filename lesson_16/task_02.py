# Атрибуты объекта и атрибуты класса

class Message:
    _id = 0

    def __init__(self, data):
        self._msg_id = type(self)._id
        self._data = data
        type(self)._id += 1

    def print(self):
        print(f"{self._data}\t id {self._msg_id} / {type(self)._id}")

    @classmethod
    def next_free_id(cls):
        return Message._id

m1 = Message("MSG 1")
m2 = Message("MSG 2")

m1.print()
m2.print()

print(Message.next_free_id())


# Методы объекта, методы класса и статические методы

class C:
    field = "class field"

    @classmethod
    def update_field(cls, new_val):
        cls.field = new_val


print(C.field)

C.update_field("new value for class field")
print(C.field)

c = C()
print(c.field)


class TestClass:
    class_field = "This is class field"

    def __init__(self):
        print("Constructor")
        self.instance_field = "This is instance field"

    def instance_method(self):
        print(f"Instance method. {self.instance_field}. {type(self).class_field}")

    @classmethod
    def class_method(cls):
        print(f"Class method. {TestClass.class_field}")

    @staticmethod
    def static_method():
        print("Static method")

tc = TestClass()

tc.instance_method()
tc.class_method()
tc.static_method()

TestClass.class_method()
TestClass.static_method()

