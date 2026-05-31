# Оператор continue

s = "Now is better than never."

for letter in s:
    if letter in "aeiouy":
        continue

    print(letter, end="")

print()


# Оператор break

s = "Although never is often better than right now."

for letter in s:
    if letter == " ":
        break

    print(letter, end="")

print()


# Ключевое слово else в связке с циклами

s = "go"

for letter in s:
    if letter == "y":
        break

    print(letter)
else:
    print("There is no letter 'y' in string")
