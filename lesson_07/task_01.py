# Вложенные функции

def outer_f():

    def inner_f():
        print("This is inner function")

    print("This is outer function")
    inner_f()

outer_f()


def create_adder(x):

    def adder(y):
        return x + y

    return adder

add_5 = create_adder(5)
result = add_5(3)
print(result)


def create_validator(threshold):
    def validate(value):
        return value >= threshold

    return validate


age_checker = create_validator(18)
score_checker = create_validator(60)

print(age_checker(25))
print(age_checker(15))
print(score_checker(70))
print(score_checker(40))


def has_permissions(directory):
    def get_permissions_str(user):
        if user == "root":
            return f"Permission to {directory} granted for {user}"

        return f"Permission to {directory} declined for {user}"

    return get_permissions_str


has_permissions_tmp = has_permissions("/tmp")
print(has_permissions_tmp("sandbox_user"))

has_permissions_logs = has_permissions("/var/logs")
print(has_permissions_logs("root"))
