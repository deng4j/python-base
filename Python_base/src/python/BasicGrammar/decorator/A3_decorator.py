"""
带参装饰器
"""


def func1(func):
    print("func1")

    def inner_f1(a):
        a += 1
        print("inner_f1正在进⾏验证 ....,a = ", a)
        func(a)  # 传递参数

    return inner_f1


def func2(func):
    print("func2")

    def inner_f2(a):
        a += 1
        print("inner_f2正在进⾏验证 ....,a = ", a)
        func(a)

    return inner_f2


@func1
@func2
def func3(a):
    print('func3：', a)


func3(10)
