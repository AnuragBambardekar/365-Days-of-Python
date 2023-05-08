import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['https://www.google.com', 'https://www.facebook.com', 'https://www.twitter.com']
    tasks = [asyncio.create_task(fetch_url(url)) for url in urls]
    responses = await asyncio.gather(*tasks) # method to wait for all tasks to complete.
    print(responses)

asyncio.run(main())
# fetch the HTML content of a URL asynchronously