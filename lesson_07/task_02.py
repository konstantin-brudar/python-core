# Замыкание (closure)

def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

say_hello = make_greeter("Привет")
say_hi = make_greeter("Хай")

print(say_hello("Анна"))
print(say_hi("Борис"))


def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter1 = create_counter()
counter2 = create_counter()

print(counter1())
print(counter1())
print(counter2())
print(counter1())


def f_outer(initial_val):
    items = [initial_val]

    def f_inner(val):
        items.append(val)
        print("Items:", items)

    return f_inner

f = f_outer(1)
f(2)
f(3)
