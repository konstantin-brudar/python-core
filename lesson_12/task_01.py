# Создание кортежей

t1 = ()
t2 = tuple()
print(type(t1), type(t2))

langs = ("haskell", "erlang", "scala")

lst = [1, 2, 3]
tpl = tuple(lst)

tpl = (128)
print(type(tpl))

tpl = (128,)
print(type(tpl))
print(tpl)


# Отличия кортежей от списков

tpl = (-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tpl[2:9:2])


words = ("upper", "level", "demand")
for w in words:
    if w == w[::-1]:
        print(w)


# Неизменяемость кортежа и ее взлом

l1 = [1, 2]
l2 = [1, 2]
t1 = (1, 2)
t2 = (1, 2)
print("l1 eq l2", l1 == l2)
print("l1 is l2", l1 is l2)
print("t1 eq t2", t1 == t2)
print("t1 is t2", t1 is t2)


t1 = (1, [], 2)
t2 = (1, [], 2)
print(t1 == t2)
print(t1 is t2)
t1[1].append("A")
print(t1)
print(t2)
print(t1 == t2)
print(t1 is t2)
