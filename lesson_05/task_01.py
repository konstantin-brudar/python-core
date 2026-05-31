# Цикл while

x = 100

while x > 0:
    print(x, end=" ")
    x -= 10

print()


# Цикл for

for x in range(10):
    print(x, end=" ")

print()


# Функция возвращает количество слов, из которых состоит строка s в snake_case

def get_words_count(s):
    if len(s) == 0:
        return 0

    words_count = 1

    for letter in s:
        if letter == "_":
            words_count += 1

    return words_count

print(get_words_count("not_supported_format"))
print(get_words_count("naive_solution"))
print(get_words_count("word"))
print(get_words_count(""))
