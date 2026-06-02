# Строки

empty1 = ""
empty2 = str()

server = "localhost:9092"

text = 'ABC'
text = "ABC"
text = '''ABC'''
text = """ABC"""

str_descr = """Textual data in Python is handled with str objects, or strings.
Strings are immutable sequences of Unicode code points.

Citation from docs.python.org
"""

s = str(3 + 5j)

a = "TEXT"
b = a
print(a)
print(id(a))
print(b)
print(id(b))
b += "2"
print(a)
print(id(a))
print(b)
print(id(b))


# Посимвольный доступ

text = "This is an example of english text."

c = text[3]
print(c)

for c in text:
    print(c, end="")
print()

for i in range(len(text)):
    print(text[i], end="")
print()


# Срезы

s = "ABCDEF"
print(s[2:4])
print(s[::3])
print(s[:-2])
print(s[:-1])
print(s[::])
print(s[::-1])
s_copy = s[:]