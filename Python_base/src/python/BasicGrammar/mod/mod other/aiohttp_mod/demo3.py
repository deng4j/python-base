import time
import asyncio
from aiohttp import ClientSession

"""
把响应一一收集到一个列表中，最后保存到本地或者打印出来。
"""

tasks = []
url = "https://www.baidu.com/{}"


async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            #      print(response)
            print('Hello World:%s' % time.time())
            return await response.read()


def run():
    for i in range(5):
        task = asyncio.ensure_future(hello(url.format(i)))
        tasks.append(task)
    result = loop.run_until_complete(asyncio.gather(*tasks))
    print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run()
