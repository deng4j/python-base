"""
原装饰器基础上设置外部变量
"""


def func1(s):
    print("func1")

    def inner_f1(func):
        print("inner_f1")

        def inner_f2(a):
            print("inner_f2")
            print("正在进⾏验证 ....,a = ", a, s)
            return func(a)

        return inner_f2

    return inner_f1


@func1("login")
def func3(a):
    print('func3：', a)


func3(10)
