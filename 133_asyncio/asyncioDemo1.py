import asyncio

async def print_numbers():
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(1)

asyncio.run(print_numbers())
# output the numbers 1 to 10, with a 1-second delay between each number.