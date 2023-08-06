import asyncio
import api

async def send_data(to: str):
    print(f"Sending Data to {to}...")
    await asyncio.sleep(2)
    print(f"Data sent to {to}!")

async def main():
    data = await api.fetch_data()
    print('Data: ', data)

    # Synchronous
    # await send_data('Bob')
    # await send_data('Alice')

    # Asycnhronous
    await asyncio.gather(send_data('Bob'),send_data('Alice'))

if __name__ == "__main__":
    asyncio.run(main())