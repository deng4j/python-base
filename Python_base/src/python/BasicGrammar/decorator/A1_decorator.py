"""
装饰器：在不改变函数的代码前提下，给函数添加新的功能。

装饰器使⽤前提：
    1、存在闭包（⽤于扩展新的功能）
    2.待扩展的普通函数 （⽬的就是不改变该函数，还增加新的功能）
"""


def func1(func):
    print("func1")

    def inner_f1():
        print("inner_f1")

    func()  # 传递是被修饰的函数
    return inner_f1


@func1
def func2():
    print('func2')


func2()
