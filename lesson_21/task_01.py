# Мотивация

try:
    f = open("urls.txt", "a")
    f.write("https://senjun.ru/courses\n")
finally:
    f.close()


# Контекстные менеджеры и оператор with

with open("urls.txt", "a") as f:
    f.write("https://senjun.ru/courses\n")


messages = ["msg1", "msg2"]

with open("messages.txt", "w") as f_out:
    with open("messages_uppercase.txt", "w") as f_out_upper:
        for msg in messages:
            f_out.write(f"{msg}\n")
            f_out_upper.write(f"{msg.upper()}\n")

with (open("messages.txt", "w") as f_out,
      open("messages_uppercase.txt", "w") as f_out_upper):
    for msg in messages:
        f_out.write(f"{msg}\n")
        f_out_upper.write(f"{msg.upper()}\n")


# Протокол контекстного менеджера

class SenjunFile:
    def __init__(self, filepath, mode):
        self.filepath = filepath
        self.mode = mode

    def __enter__(self):
        print(f"Opening {self.filepath}")
        self.__file = open(self.filepath, self.mode)
        return self.__file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f"Closing {self.filepath}")
        if not self.__file.closed:
            self.__file.close()

        return False

with SenjunFile("urls.txt", "r") as file:
    for line in file:
        print(line.strip())
    file.close()


import sys

class StdoutRedirected:
    def __init__(self, stdout_replacement):
        self.__stdout = sys.stdout
        self.__stdout_replacement = stdout_replacement

    def __enter__(self):
        sys.stdout = self.__stdout_replacement

    def __exit__(self, exc_type, exc_value, exc_traceback):
        sys.stdout = self.__stdout
        return False

print("---> stdout")

with open("output.txt", "w") as f:
    with StdoutRedirected(f):
        print("---> file")

print("---> stdout again")
