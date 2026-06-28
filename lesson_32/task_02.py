# Ожидание выполнения самой быстрой задачи

import asyncio
import time

async def task_coro(value):
    await asyncio.sleep(value)
    print(f"> task '{value}' done")

async def main():
    start = time.time()
    print("main starting")
    tasks = [asyncio.create_task(task_coro(i)) for i in range(5)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print("done waiting for first completed task")
    await asyncio.sleep(5)
    print(f"main completed in {time.time() - start:.4f} seconds")

asyncio.run(main())


# Асинхронный контекстный менеджер

import asyncio

class AsyncContextManager:
    async def __aenter__(self):
        print("read big file...")
        await asyncio.sleep(2)

    async def __aexit__(self, exc_type, exc, tb):
        print("async manager exited")

async def tick():
    while True:
        print("tick")
        await asyncio.sleep(0.5)

async def main():
    asyncio.create_task(tick())
    async with AsyncContextManager() as m:
        print("inside async with")

asyncio.run(main())


# Асинхронный итератор

import asyncio

class AsyncIterator:
    def __init__(self):
        self.counter = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.counter >= 2:
            raise StopAsyncIteration

        self.counter += 1
        await asyncio.sleep(1)

        return self.counter

async def coro():
    while True:
        print("Tick")
        await asyncio.sleep(0.5)

async def main():
    _ = asyncio.create_task(coro())
    async for item in AsyncIterator():
        print(item)

asyncio.run(main())
