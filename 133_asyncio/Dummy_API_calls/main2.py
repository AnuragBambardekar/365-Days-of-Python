import asyncio
import api

async def main():
    task = asyncio.create_task(
        api.fetch_data()
    )

    # task.cancel()
    # await asyncio.sleep(0.5)

    # if task.cancelled():
    #     print(task.cancelled())

    try:
        # if task.done():
        #     print(task.result())

        await asyncio.wait_for(task, timeout=10)

        result = await task
        print(result)
    except asyncio.CancelledError:
        print("CANCELLED: Request was cancelled...")
    except asyncio.TimeoutError:
        print("TIMEOUT: Request took too long...")

if __name__ == "__main__":
    asyncio.run(main())