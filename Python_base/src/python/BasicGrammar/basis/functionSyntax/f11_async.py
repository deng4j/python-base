import time
import asyncio

"""
asyncio函数：异步IO采用消息循环的模式，重复“读取消息—处理消息”的过程，也就是说异步IO模型”需要一个消息循环，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程。

event_loop 事件循环：程序开启一个无限的循环，程序员会把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。

coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。

task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。

async/await 关键字： 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。


async def 用来定义异步函数，其内部有异步操作。每个线程有一个事件循环，主线程调用asyncio.get_event_loop()时会创建事件循环，
    把异步的任务丢给这个循环的 run_until_complete()方法，事件循环会安排协同程序的执行。
    
tasks = [] 任务则是对协程进一步封装，其中包含任务的各种状态。即多个coroutine函数可以封装成一组Task然后并发执行。

loop = asyncio.get_event_loop() #获取“事件循环”对象

loop.close() 结束时间循环。
"""


# 定义异步函数
async def hello():
    print('Hello World1111:%s' % time.time())
    # 必须使用await，不能使用yield from；如果是使用yield from ，需要采用@asyncio.coroutine相对应
    await asyncio.sleep(1)
    print('Hello wow World2222:%s' % time.time())


def run():
    tasks = []
    for i in range(5):
        tasks.append(hello())
    loop.run_until_complete(asyncio.wait(tasks))


loop = asyncio.get_event_loop()
if __name__ == '__main__':
    run()
