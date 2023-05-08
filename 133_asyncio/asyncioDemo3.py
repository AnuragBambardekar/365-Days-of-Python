## Synchronous Way
# import time

# def func1():
#     time.sleep(3)
#     print("func 1")

# def func2():
#     time.sleep(3)
#     print("func 2")

# def func3():
#     time.sleep(3)
#     print("func 3")

# func1()
# func2()
# func3()

## Asynchronous Way
import time
import asyncio

async def func1():
    await asyncio.sleep(1)
    print("func 1")
    return "Bamba"

async def func2():
    await asyncio.sleep(1)
    print("func 2")

async def func3():
    await asyncio.sleep(4)
    print("func 3")

async def main():
    # task = asyncio.create_task(func1())
    # # await func1()
    # await func2()
    # await func3()

    L = await asyncio.gather(func1(), func2(), func3())
    print(L)

asyncio.run(main=main())