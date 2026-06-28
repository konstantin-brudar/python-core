# Модуль concurrent.futures

import time
from concurrent.futures import ProcessPoolExecutor

def calc_and_sleep(a, b):
    time.sleep(1)
    return pow(a, b)

start = time.perf_counter()

with ProcessPoolExecutor(max_workers=1) as executor:
    future = executor.submit(calc_and_sleep, 128, 256)
    print(future.result())

finish = time.perf_counter()
print(f"Finished in {finish - start:.2f} seconds")


# Методы запуска процессов: fork (только Unix/Linux)

from multiprocessing import get_context

ctx = get_context('fork')
with ProcessPoolExecutor(mp_context=ctx) as executor:
    ...


# Методы запуска процессов: spawn (все платформы)

from multiprocessing import get_context

ctx = get_context('spawn')
if __name__ == "__main__":
    with ProcessPoolExecutor(mp_context=ctx) as executor:
        ...


# Методы запуска процессов: forkserver (Unix/Linux, по умолчанию в Python 3.14+)

from multiprocessing import get_context

ctx = get_context('forkserver')
with ProcessPoolExecutor(mp_context=ctx) as executor:
    ...


# Кроссплатформенная работа

from multiprocessing import get_context

try:
    ctx = get_context('fork')
except ValueError:
    ctx = get_context('spawn')

if __name__ == "__main__":
    with ProcessPoolExecutor(mp_context=ctx) as executor:
        ...


# Модуль multiprocessing

from multiprocessing import Pool

if __name__ == '__main__':
    with Pool(3) as p:
        print(p.map(abs, [-2, 8, -3, 0]))


from multiprocessing import Process

if __name__ == '__main__':
    p = Process(target=print, args=("text",))
    p.start()
    p.join()


from multiprocessing import Process, Queue

def f(q, x):
    q.put([x*2, x*3])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q, 3))
    p.start()
    print(q.get())
    p.join()


from multiprocessing import Process, Pipe

def f(conn):
    while True:
        x = conn.recv()
        if x is None:
            return

        conn.send(x * 2)

if __name__ == '__main__':
    conn_parent, conn_child = Pipe()
    p = Process(target=f, args=(conn_child,))
    p.start()

    for val in [3, 4, 5]:
        conn_parent.send(val)
        print(conn_parent.recv())

    conn_parent.send(None)
    p.join()


import random
import time
from multiprocessing import Process, Lock

def f(lock, i):
    time.sleep(random.randint(0, 6))

    lock.acquire()

    try:
        print("Process #", i)
    finally:
        lock.release()

if __name__ == '__main__':
    lock = Lock()

    for i in range(1, 6):
        Process(target=f, args=(lock, i)).start()


# Потоки

from time import sleep
from threading import Thread, Lock

def f(n, lock1, lock2):
    print(f"Thread {n} acquiring lock 1...")

    with lock1:
        sleep(1)
        print(f"Thread {n} acquiring lock 2...")

        with lock2:
            print(f"Thread {n} acquired 2 locks!")

lock_a = Lock()
lock_b = Lock()

t1 = Thread(target=f, args=(1, lock_a, lock_b))
t2 = Thread(target=f, args=(2, lock_a, lock_b))

t1.start()
t2.start()

t1.join()
t2.join()
