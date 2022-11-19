import asyncio
from aiohttp import ClientSession

"""
如果需要并发http请求，通常是用requests，但requests是同步的库，如果想异步的话需要引入aiohttp。


"""

tasks = []
url = "https://www.baidu.com/{}"


async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello(url))
