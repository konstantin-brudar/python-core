# Счетчик ссылок

from sys import getrefcount

d = {}
d2 = d

print(getrefcount(d))


# Субинтерпретаторы (subinterpreters)

from concurrent import interpreters
# Создание и запуск кода
interp = interpreters.create()
interp.exec("print('Hello from subinterpreter!')")
# Обмен данными через кросс-интерпретаторную очередь
q = interpreters.create_queue()
interp.prepare_main(out=q)
interp.exec("""
for i in range(5):
    out.put(i * i)
""")
# Получение результатов в основном интерпретаторе
results = []
for _ in range(5):
    results.append(q.get())
print(results)
# Обязательно закрываем интерпретатор
interp.close()


from concurrent.futures import InterpreterPoolExecutor
def square(x):
    return x * x
with InterpreterPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(square, range(5)))
print(results)


# Free-threaded Python

import sys
# Проверка, включён ли GIL (доступно в Python 3.13+)
if hasattr(sys, '_is_gil_enabled'):
    print(f"GIL enabled: {sys._is_gil_enabled()}")
else:
    print("Free-threaded build not detected")
