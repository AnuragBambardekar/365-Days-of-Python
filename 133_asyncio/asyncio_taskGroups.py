import asyncio

async def count(n):
    for i in range(1, n+1):
        print(i)
        await asyncio.sleep(0)
    return n

async def main():
    # a context manager that we can add tasks to
    # raises an exception group when error occurs

    # only available in 3.11
    async with asyncio.TaskGroup() as tg: # replaces asyncio.gather
        t1 = tg.create_task(count(5))
        t2 = tg.create_task(count(10))
        # Returns Exception Group
        # with async.gather we would've got only the first exception
        tg.create_task(count("4"))
        tg.create_task(count(1.5))

    # print(t1.result())
    # print(t2.result())

    print("All Done!")

asyncio.run(main())