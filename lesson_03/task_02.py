title = "The walrus operator"
words_count = len(title.split())

if words_count > 10:
    print("Too many words in paragraph title:", words_count)
else:
    print("Paragraph title is suitable. Words count:", words_count)


# Оператор моржа (walrus)

title = "The walrus operator"

if (words_count := len(title.split())) > 10:
    print("Too many words in paragraph title:", words_count)
else:
    print("Paragraph title is suitable. Words count:", words_count)


# Популярный сценарий использования

print("Status code:", code := 200)
print(code)


# Замечание про f-строки

def print_and_len(obj):
    print(f"{(s := obj)}\n{len(s)}")

print_and_len("hello")


# Создание переменных при вызове функции

print(min(a := 8, b := -2, c := 4, d := 0))
