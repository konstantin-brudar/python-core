# Скалярные типы данных

month = 12
day = 31

number_binary = 0b1101
nummber_octal = 0o732
nummber_hex = 0xAFF9

a = 1
b = 2
a = b
res = a + b
res = a - b
a += 1
a -= 1
res = a * b
res = a / b
res = a // b
res = a % b
res = a ** b
res = pow(a, b)
res = -a
res = +a

a *= b
a /= b

a = 1
abs(a)
round(a, b)
divmod(a, b)
bin(a)
oct(a)
hex(a)
print(int('FF', 16))

a = 1
b = 2
res = a > b
res = a >= b
res = a < b
res = a <= b
res = a == b
res = a != b

val = 7
if 0 < val <= 12:
    print("...this value may be month")

a = 1
b = 2
res = a & b
res = a | b
res = ~a
res = a ^ b
res &= 0b110000
res = a << b
res = a >> b

def is_eq_abs(a, b, eps):
    return abs(a - b) < eps

print(is_eq_abs(37.001, 37.002, 0.1))
print(is_eq_abs(37.001, 37.002, 1e-5))

a = True
b = False
a = 10 > 9
b = 2 == 3
res = a and b or not a

print(id(True))
print(id(2 * 2 == 4))

discount = None

def safe_get_int(x):
    try:
        return int(x)
    except ValueError:
        return None

print(safe_get_int("20"))
print(safe_get_int("here we get nothing"))

x = None
if x is None:
    print("Got None for x")

x = 1
if x is not None:
    print("x is not None")

x = 256
y = 256
print(x == y)
print(x is y)
