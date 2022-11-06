import random
import asyncio

b = 3 * random.randrange(3, 20)
k =1 

async def EverySecond()-> None:
    global k
    k = 1
    while k < b:

        await asyncio.sleep(1)

        if k%3!=0:
            print(f"Прошло {k} секунд")
        k=k+1

async def EveryThreeSecond()-> None:
    global k
    while k < b:

        await asyncio.sleep(3)
        
        print("Прошло еще 3 секунды")
    return None

async def main() -> None:

    task_1 = asyncio.create_task(EverySecond())
    task_2 = asyncio.create_task(EveryThreeSecond())

    await task_1
    await task_2

    return None

asyncio.run(main())