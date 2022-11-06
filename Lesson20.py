import random
import asyncio

b = 3 * random.randrange(3, 200)
k =1 

async def EverySecond():
    global k
    k = 1
    while k < b:

        await asyncio.sleep(1)

        if k%3!=0:
            print(f"Прошло {k} секунд")
        k=k+1
    return None

async def EveryThreeSecond():
    global k
    while k < b:

        await asyncio.sleep(3)
        
        print("Прошло еще 3 секунды")
    return None

async def main():

    task_1 = asyncio.create_task(EverySecond())
    task_2 = asyncio.create_task(EveryThreeSecond())

    await task_1
    await task_2

    return None

asyncio.run(main())