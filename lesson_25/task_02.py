# Упаковка

a, _, b = ["a", "x", "b"]
print(a, _, b)


_, second, third, _ = (1, 2, 3, 4)
print(second, third, _)


*_, last = [1, 2, 3, 4, 5]
print(_)
print(last)
print(type(_))


first, *_, last = "import this"
print(first, last)


lst = [1, 2, 3, 4]
a, b, *_, c, d = lst
print(a, b, c, d)
print(_)


*vals, = 1, 2, 3
print(vals)
print()


containers = ["tuple", "set", "list", "dict"]
_, (head, *tail), *_ = containers
print(_)
print(head)
print(tail)


style = ["primary color", (3, 161, 252, 0.5)]
title, [r, g, b, a] = style
print(title)
print(r, g, b, a)


# Объединение итерабельных объектов

head = [1, 2]
tail = [3, 4, 5]
merged = head + tail
print(merged)


head = [1, 2]
tail = [3, 4, 5]
merged = [*head, *tail]
print(merged)


head = [1, 2]
tail = [3, 4, 5]
merged = [*head, 0, *tail, 0, 0]
print(merged)


s1 = {1, 3, 4}
s2 = {2, 3, 4, 5, 6}
merged = {*s1, *s2, 10, 20}
print(merged)


d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"c": 4, "d": 5}
d3 = {"d": 6, "e": 7}
merged = {**d1, **d2, **d3}
print(merged)
merged = {**d3, **d2, **d1}
print(merged)


# Распаковка аргументов функций

def weather_forecast(city, date):
    print(city, date)

weather_forecast("Omsk", "tomorrow")

weather_forecast(*("Omsk", "tomorrow"))

lst = ["Omsk", "tomorrow"]
weather_forecast(*lst)

weather_forecast(city="Omsk", date="tomorrow")

weather_forecast(**{"city":"Omsk", "date":"tomorrow"})
weather_forecast(**dict((("city", "Omsk"), ("date", "tomorrow"))))

d = {"city":"Omsk", "date":"tomorrow"}
weather_forecast(**d)
