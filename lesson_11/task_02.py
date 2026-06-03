# Распространенные операции над списками

if -1 in [8, -1, 93]:
    print("list contains -1")


lst = ["a", "b"]
print(lst * 4)


m = ["dart", "carbon"]
l = ["kotlin"]
l = m + l
print(l)


temperatures = [23.2, 21.0, 19.9, 22.5]
min_temp = min(temperatures)
print(min_temp)


x = ["assert", "bool", "false"]
del x[1]
print(x)


words = "Sparse is better than dense".split()
del words[1:-1]
print(words)


# Распространенные методы списков

l = [1, 2, 3]

x = 4
l.append(x)

i = 1
l.insert(i, x)

l2 = [5, 6, 7]
l.extend(l2)

x = 5
l.remove(x)

i = -1
res = l.pop(i)

l.clear()

l.sort(key=None, reverse=False)


words = ["clear", "pop", "append"]
words.sort(key=len, reverse=True)
print(words)


res = ["Errors", "should", "never", "pass"]
res += "silently"
res.append("silently")
print(res)


words = ["simple", "is", "better", "than", "complex"]
citation = " ".join(words)
print(citation)


# Изменяемые типы как аргументы функции по умолчанию

def add_word(word, words=[]):
    words.append(word.lower().strip())
    print(words)

add_word("Simple")
add_word("Complex")


def add_word(word, words=None):
    words = []
    words.append(word.lower().strip())
    return words

print(add_word("Simple"))
print(add_word("Complex"))
