"""
闭包（closure）：在⼀个外函数中定义了⼀个内函数，内函数⾥运⽤了外函数的临时变量，
    并且外函数的返回值是内函数的引⽤。这样就构成了⼀个闭包。
"""


def func1(x):
    print("func1() - x：", x)

    def func2(y):
        print("func2() - x：", x)
        print("func2() - y：", y)

    return func2


func_ = func1(10)
func_(20)
