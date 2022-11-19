import gevent

"""
greenlet已经实现了协程，但是这个还的⼈⼯切换，是不是觉得太麻烦了，其原理是
当⼀个greenlet遇到IO(指的是input output 输⼊输出，⽐如⽹络、⽂件操作等)操作时， 
⽐如访问⽹络，就⾃动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执⾏。
由于IO操作⾮常耗时，经常使程序处于等待状态，有了gevent为我们⾃动切换协程，
就保证总有 greenlet在运⾏，⽽不是等待IO

介绍:Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是Greenlet，
它是以C扩展模块形式接入Python的轻量级协程。 Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。

g1=gevent.spawn(func,1,,2,3,x=4,y=5)：创建一个协程对象g1，spawn括号内第一个参数是函数名，
如eat，后面可以有多个参数，可以是位置实参或关键字实参，都是传给函数eat的

g1.join()：等待g1结束

g1.value：拿到func1的返回值
"""

print("---------------------- 遇到io主动切换 -------------------")


def eat(name):
    print('%s eat 1' % name)
    # gevent.sleep(2)模拟的是gevent可以识别的io阻塞，而time.sleep(2)或其他的阻塞，gevent是不能直接识别的需要用from gevent import monkey;monkey.patch_all()，放在第一行
    gevent.sleep(2)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    gevent.sleep(1)
    print('%s play 2' % name)


g1 = gevent.spawn(eat, 'egon')
g2 = gevent.spawn(play, name='egon')
g1.join()
g2.join()
# 或者gevent.joinall([g1,g2])
print('主线程结束')
