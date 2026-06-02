# Изменяемые и неизменяемые типы

lang = "ru"
print(id(lang))

is_connected = True
print(type(is_connected))


count = 5
print(type(count))
print(id(count))
count += 1
print(type(count))
print(id(count))


nums = [5]
print(type(nums))
print(id(nums))
nums.append(1)
print(type(nums))
print(id(nums))


# Создание объектов

x = False
x = bool()
x = bool(9.9)
x = int(3.14)
x = int("255")
