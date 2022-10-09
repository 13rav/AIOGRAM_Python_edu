import random
import asyncio

b = 3 * random.randrange(3, 200)
k =1 

async def EverySecond():
    global k
    k = 1
    while k < b:
        await asyncio.Sleep(1)
        print(f"Прошло {k} секунд")
        k=k+1
    return None

async def EveryThreeSecond():
    global k
    while k < b:
        await asyncio.Sleep(3)
        rint(f"Прошло {k} секунд")
    return None

async def main():

    task_1 = asyncio.create_task(EverySecond())
    task_1 = asyncio.create_task(EveryThreeSecond())
    return None

asyncio.run(main())