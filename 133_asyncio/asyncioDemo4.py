import time
import asyncio
import requests



async def func1():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram1.ico","wb").write(response.content)
    print("func 1")
    return "Bamba"

async def func2():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram2.ico","wb").write(response.content)
    print("func 2")

async def func3():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram3.ico","wb").write(response.content)
    print("func 3")

async def main():
    # Slower
    # await func1()
    # await func2()
    # await func3()

    # Faster
    L = await asyncio.gather(func1(), func2(), func3())
    print(L)

asyncio.run(main=main())