# Определение класса как исполняемое выражение

class SideEffect:
    def __init__(self):
        print("Side effect")

print("Before class definition")

class Test:
    test_class_field = SideEffect()

print("After class definition")


def send_sms():
    print("Sending sms...")

class BadBadClass:
    for i in range(3):
        send_sms()

print("After class definition")
