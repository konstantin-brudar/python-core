# Асинхронность

import concurrent.futures
import time

def worker1():
    print("worker1 begins")
    time.sleep(2)
    print("worker1 done")

def worker2():
    print("worker2 begins")
    time.sleep(1)
    print("worker2 done")

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(worker1)
    f2 = executor.submit(worker2)
    print("asynchronous tasks started")
    concurrent.futures.wait([f1, f2])

