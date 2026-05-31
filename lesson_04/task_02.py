# Сопоставления с образцом (pattern matching)

val = 8

match val:
    case 0:
        print('OK')
    case 1:
        print('Error')
    case unknown_val:
        print('Unexpected value:', unknown_val)


def parse_option(option):
    match option:
        case "save_to_file":
            return "Saving data to file..."
        case "log_statistics":
            return "Dumping stats to logs..."
        case "quit":
            return "Quitting..."
        case _:
            return "Unsupported option"

print(parse_option("exit"))
print(parse_option("quit"))


# Приложение ожидает команду (exit, copy, delete) и дополнительные опции от пользователя

user_input = input("Please enter command: ")
commands = user_input.split()

match commands:
    case ["exit"]:
        exit(0)
    case ["copy", path_src, path_dst]:
        print(f"Copying file from {path_src} to {path_dst}...")
    case ["delete", path]:
        print(f"Deleting file {path}...")
    case _:
        print ("Unsupported command", user_input)
