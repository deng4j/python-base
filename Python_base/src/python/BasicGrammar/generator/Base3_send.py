"""
协同程序（协程）一般来说是指这样的函数：
    1.彼此间有不同的局部变量、指令指针，但仍共享全局变量；
    2.可以方便地挂起、恢复，并且有多个入口点和出口点；
    3.多个协同程序间表现为协作运行，如A的运行过程中需要B的结果才能继续执行。

协程的特点决定了同一时刻只能有一个协同程序正在运行（忽略多线程的情况）。得益于此，
协程间可以直接传递对象而不需要考虑资源锁、或是直接唤醒其他协程而不需要主动休眠，
就像是内置了锁的线程。在符合协程特点的应用场景，使用协程无疑比使用线程要更方便。

send()是除next()外另一个恢复生成器的方法。Python2.5+中，yield语句变成了yield表达式，这意味着
yield现在可以有一个值，而这个值就是在生成器的send方法被调用从而恢复执行时，调用send方法的参数。

使⽤ send()函数的⼀个好处是可以在唤醒的同时向断点处传⼊⼀个附加数据。c.next()等价c.send(None)

调用send传入非None值前，生成器必须处于挂起状态，否则将抛出异常。不过，未启动的生成器仍可以使用None作为参数调用send。
如果使用next恢复生成器，yield表达式的值将是None。
"""


def h():
    print('--start--')
    first = yield 5  # 等待接收 Fighting! 值
    print('1', first)
    second = yield 12  # 等待接收 hahaha! 值
    print('2', second)
    yield 13
    print('--end--')


g = h()
first = next(g)  # m 获取了yield 5 的参数值 5
# (yield 5)表达式被赋予了'Fighting!',  d 获取了yield 12 的参数值12
second = g.send('Fighting!')
third = g.send('hahaha!')  # (yield 12)表达式被赋予了'hahaha!'
print(f'--over--')
print(f"first:{first}, second:{second}, third:{third}")
