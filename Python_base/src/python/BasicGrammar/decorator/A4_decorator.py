"""
装饰的函数有返回值
"""


def func1(func):
    print("func1")

    def inner_f1(a):
        a += 1
        print("inner_f1正在进⾏验证 ....,a = ", a)
        return func(a)  # 返回值，否则最终结果是None

    return inner_f1


def func2(func):
    print("func2")

    def inner_f2(a):
        a += 1
        print("inner_f2正在进⾏验证 ....,a = ", a)
        return func(a)

    return inner_f2


@func1
@func2
def func3(a):
    print('func3：', a)
    return a


x = func3(10)
print(x)
