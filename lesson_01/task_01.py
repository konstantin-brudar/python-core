# Неявная типизация

code_ok = 200
response_ok = "OK"

err_service_unavailable = 503

# Динамическая типизация

res = True
res = "Success"
res = -1

# Строгая типизация

print("Returned HTTP code " + str(200))


# Отступы

new_items = [2, 8, 6]
for item in new_items:
    print(item)


matrix = list()

for i in range(0, 5):
    matrix.append(list())
    for j in range(0, 5):
        matrix[i].append(i * j)

print(matrix)


# Python 3

x = 3//2
print(x)
