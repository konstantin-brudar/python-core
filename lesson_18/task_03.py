# Внутреннее представление атрибутов объекта

class Example:
    _id_cls = 0

    def __init__(self):
        self._id_obj = 0

print("Class attributes:", Example.__dict__)
print("Instance attributes:", Example().__dict__)


print("Class list attributes:")
for key, value in list.__dict__.items():
    print(f"{key} {value}")


# Monkey patching

class DataRow:
    pass

dr = DataRow()
old_attrs = set(dr.__dict__)

dr.field = "VALUE"
new_attrs = set(dr.__dict__)

diff_attrs = new_attrs - old_attrs

print("New attributes:")
for attr in diff_attrs:
    print(f"{attr} {dr.__dict__[attr]}")
