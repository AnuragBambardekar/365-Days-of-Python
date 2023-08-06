import asyncio

async def main():
    task = asyncio.create_task(other_func()) # this task is now scheduled
    # once we have some idle time, the task is going to be called
    print("A")
    await asyncio.sleep(1)
    print("B")
    return_value = await task # to get the value of return
    print(f"Return Value: {return_value}")

async def other_func():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10

asyncio.run(main())

