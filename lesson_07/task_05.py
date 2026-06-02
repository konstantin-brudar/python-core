# Функции как объекты первого класса

def greet(name):
    return f"Привет, {name}!"

hello_func = greet
print(hello_func("Мир"))


def square(x):
    return x * x

def cube(x):
    return x * x * x

functions = [square, cube]
for func in functions:
    print(func(3))


def apply_operation(value, operation):
    return operation(value)

def double(x):
    return x * 2

result = apply_operation(5, double)
print(result)
