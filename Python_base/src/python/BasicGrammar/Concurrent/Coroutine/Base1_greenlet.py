from greenlet import greenlet

"""
协程：是单线程下的并发，又称微线程，纤程。英文名Coroutine。协程是一种用户态的轻量级线程，即协程是由用户程序自己控制调度的。

需要强调的是：
    1.python的线程属于内核级别的，即由操作系统控制调度（如单线程遇到io或执行时间过长就会被迫交出cpu执行权限，切换其他线程运行）
    2.单线程内开启协程，一旦遇到io，就会从应用程序级别（而非操作系统）控制切换，以此来提升效率（！！！非io操作的切换与效率无关）
    3.对比操作系统控制线程的切换，用户在单线程内控制协程的切换。

优点如下：
    1.协程的切换开销更小，属于程序级别的切换，操作系统完全感知不到，因而更加轻量级
    2.单线程内就可以实现并发的效果，最大限度地利用cpu
缺点如下：
    1.协程的本质是单线程下，无法利用多核，可以是一个程序开启多个进程，每个进程内开启多个线程，每个线程内开启协程
    2.协程指的是单个线程，因而一旦协程出现阻塞，将会阻塞整个线程

协程特点：
    1.必须在只有一个单线程里实现并发
    2.修改共享数据不需加锁
    3.用户程序里自己保存多个控制流的上下文栈
    4.附加：一个协程遇到IO操作自动切换到其它协程（如何实现检测IO，yield、greenlet都无法实现，就用到了gevent模块（select机制））
    
Swich：
    一个Greenlet是一个很小的独立微线程，可以把它想象成一个堆栈帧，栈底是初始调用，栈顶是当前Greenlet的暂停位置，
    使用Greenlet创建一堆这样的堆栈，然后在它们之间跳转执行。跳转并不是绝对的，因为一个Greenlet必须选择跳转到选择好的另一个Greenlet，
    这会让前一个挂起，而后一个恢复，两个Greenlet之间的跳转又被称之为切换switch。

libev
    是一个高性能的事件循环event loop实现。事件循环（IO多路复用）是解决阻塞问题实现并发的一种方式。事件循环event loop会捕获并处理IO事件的变化，
    当遇到阻塞时就会跳出，当阻塞结束时则会继续。这一点依赖于操作系统底层的select函数及其升级版poll和epoll。而Greenlet则是一个Python的协程管理和切换的模块，
    通过Greenlet可以显式地在不同的任务之间进行切换。

Monkey-patching
    使用猴子补丁的方式Gevent能够修改标准库中大部分的阻塞式系统调用，包括socket、ssl、threading、select等模块，使其变为协作式运行。
    Monkey-patching猴子补丁是将标准库中大部分的阻塞式调用替换成非阻塞的方式，包括socket、ssl、threading、select、httplib等。
    通过monkey.path_xxx()函数来打补丁，根据Gevent文档中的建议，应当将猴子补丁的代码尽可能早的被调用，这样可以避免一些奇怪的异常。

generator实现的协程在yield value时只能将value返回给调⽤者(caller)。 
⽽在greenlet中， target.switch（value）可以切换到指定的协程（target）， 
然后yield value。greenlet⽤switch来表示 协程的切换，从⼀个协程切换到另⼀个协程需要显式指定。
    
下载模块：pip3 install greenlet
"""

print("-------------- greenlet实现状态切换 ----------------")


# 单纯的切换（在没有io的情况下或者没有重复开辟内存空间的操作），反而会降低程序的执行速度。

def eat(name):
    print('%s eat 1' % name)
    g2.switch('nick')
    print('%s eat 2' % name)
    g2.switch()


def play(name):
    print('%s play 1' % name)
    g1.switch()
    print('%s play 2' % name)


g1 = greenlet(eat)
g2 = greenlet(play)

g1.switch('nick')  # 可以在第一次switch时传入参数，以后都不需要
