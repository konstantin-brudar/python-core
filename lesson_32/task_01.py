# Корутины и синтаксис async/await

async def coro_100():
    print(100)

async def coro_42():
    await coro_100()
    print(42)

def main():
    try:
        c = coro_42()
        c.send(None)
    except StopIteration:
        pass
    print("main ended")

main()


import asyncio

async def coro_100():
    print(100)

async def coro_42():
    await coro_100()
    print(42)

async def main():
    await coro_42()
    print("main ended")

asyncio.run(main())


# Задачи

import asyncio

async def coroutine_task():
    print("task started")
    await asyncio.sleep(1)

async def main():
    print("main coroutine")
    task = asyncio.create_task(coroutine_task())
    await task

asyncio.run(main())
print("main ended")


import asyncio

async def coro():
    print("Hi, coro!")
    await asyncio.sleep(0)
    print("Bye, coro!")

async def long_calculation():
    print("Long calculation")
    await asyncio.sleep(1)
    print("Long calculation done")

async def main():
    _ = asyncio.create_task(coro())
    t2 = asyncio.create_task(long_calculation())
    await t2

asyncio.run(main())


# Ожидание выполнения группы задач

import asyncio

async def coro(number):
    print(f"> task {number} executing")
    await asyncio.sleep(0.5)

async def main():
    tasks = [asyncio.create_task(coro(i)) for i in range(5)]
    for task in tasks:
        await task

asyncio.run(main())


async def main():
    tasks = [asyncio.create_task(coro(i)) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())
