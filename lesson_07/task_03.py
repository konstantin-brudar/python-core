# Лямбда-функции

double = lambda x: x * 2
print(double(5))

add = lambda x, y: x + y
print(add(3, 4))

greet = lambda: "Привет, мир!"
print(greet())

mult_str = lambda s, n:  s * n
print(mult_str("*", 5))

(lambda s, n:  print(s * n))("I", 3)
