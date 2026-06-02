# Распространенные операции над строками

s = "some text"
s1 = "string 1"
s2 = s1
is_equal = s1 == s2
c = s[2]
slice = s[2:8:3]
slice = s[2:8]
is_in_string = c in s
is_not_in_string = c not in s
s = s1 + s2
s1 += s2
repetition = s * 8
repetition = 8 * s

s = "something"
print(len(s))
print(min(s))
print(max(s))


# Распространенные методы строк

s = "This is an example of english text"
c = "is"
res = s.count(c)
res = s.startswith(c)
res = s.endswith(c)
res = s.upper()
res = s.lower()
res = s.isnumeric()
res = s.find(c)
res = s.rfind(c)
res = s.strip()
src = "english"
target = "russian"
res = s.replace(src, target)
res = s.split()
delim = ","
seq = ["A", "B"]
res = delim.join(seq)
encoding="cp1251"
res = s.encode(encoding)


# Форматирование строк

s = "ABC"

print("String "  + s + " has " + str(len(s)) + " letters")

print("String %s has %d letters" % (s, len(s)))

print("String {} has {} letters".format(s, len(s)))

print(f"String {s} has {len(s)} letters")


x = 5
print(f"{x=}")


from datetime import datetime

print(f"Today: {(today:=datetime.today()):%Y-%m-%d}, day of week: {today:%A}")
