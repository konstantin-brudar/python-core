# Вложенный блок — это не всегда область видимости

if True:
    x = "variable inside 'if'"

print(x)


vals = [1]
for val in vals:
    print(f"val in loop: {val}")

print(f"val after loop: {val}")


for i in range(3):
    x = i * 2

print(i)
print(x)


try:
    a = "Inside 'try'"
    raise ValueError("Some unexpected val")
except Exception as e:
    b = "Inside 'except'"

print(a)
print(b)


try:
    x = False
    assert x, "x must be True"
except AssertionError as e:
    res = e

print(res)


def f(a, b):
    res = a + b

res = f(1, 2)
print(res)


# Правило LEGB для разрешения имен

x = 1

def f():
    x = 2

    def inner():
        x = 3
        print(f"inner(): {x}")

    print(f"f(): {x}")
    inner()

print(f"global: {x}")

f()


x = 1

def f():
    # x = 2

    def inner():
        # x = 3
        print(f"inner(): {x}")

    print(f"f(): {x}")
    inner()

print(f"global: {x}")

f()
