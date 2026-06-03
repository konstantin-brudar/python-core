# Создание списка

langs = []
langs = list()

langs = ["haskell", "erlang", "scala"]

random_stuff = [2, 2, False, 9.1, ["A", 8], "search"]

links = ["realpython.com", "docs.python.org" "python.org"]
print(links)

langs = list("elixir")
print(langs)

langs = ["elixir"]


# Работа с элементами списка

sequences = ["str", "list", "tuple", "range"]
print(sequences[1])


matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
val = matrix[2][1]
matrix[1][0] = val
print(matrix)


collections = ["sequences", "sets", "mappings"]
last_val = collections[-1]
print(last_val)


l = [1, 2, "bonjour"]
m = [1, "bonjour", 2]
print(l == m)


l = [16, 32]
m = [16, 32]
print(id(l))
print(id(m))
print(l == m)


l1 = ["pointer", "reference"]
l2 = l1[:]
print(id(l1))
print(id(l2))
print(l2)


lst = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_lst = lst[::-1]
print(reversed_lst)


l = ["A", "B", "C", "D", "E", "F", "G", "H"]
l[2:5] = [10, 20, 30, 40, 50, 60]
print(l)


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("lst", lst)
sl1 = lst[1:7]
print("sl1", sl1)
sl2 = lst[2:4]
print("sl2", sl2)
sl1[1:5] = []
print("\nAfter sl1 reassignment:")
print("lst", lst)
print("sl1", sl1)
print("sl2",  sl2)
