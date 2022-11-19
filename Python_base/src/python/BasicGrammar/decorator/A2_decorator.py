"""
多重装饰器：多个装饰器装饰同⼀个函数。
"""


def func1(func):
    print("func1")

    def inner_f1():
        print("inner_f1")

    func()  # 传递是被修饰的函数
    return inner_f1


def func2(func):
    print("func2")

    def inner_f2():
        print("inner_f2")

    func()
    return inner_f2


@func1
@func2
def func3():
    print('func3')


func3()
