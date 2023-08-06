import asyncio

async def fetch_data() -> str:
    print("Fetching data...")
    await asyncio.sleep(3)
    print('Data fetched!')

    return 'API Data'