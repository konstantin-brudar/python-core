# Условные выражения

a = 3
b = 9

if a == b:
    print("a and b are equal")
elif a % b == 0:
    print("b is a divisor of a")
elif b % a == 0:
    print("a is a divisor of b")
else:
    print("else branch")


def analyze_string(s):
    print("Analyzing string...")

    if s.isdigit():
        print("All characters are digits")
    elif s.islower():
        print("All characters are lower case")
    elif s.isalpha():
        print("All characters are in the alphabet")
    else:
        print("There is nothing special about this string")

    print("Finished string analysis")


analyze_string("Hint")

# Тернарный if

code = 404
res = "OK" if code == 200 else "Error"


s = "Explicit is better than implicit."
s_descr = "long string" if len(s) > 79 else "short string"


for val in [8, 3, 16]:
    res = "even" if val % 2 == 0 else "odd"
    print(val, res)
