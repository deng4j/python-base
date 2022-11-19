a = 10
b = 11


def func1(x):
    c = 12

    def func2():
        d = 13
        print("func2() - a：", a)
        print("func2() - b：", b)
        print("func2() - c：", c)
        print("func2() - d：", d)

    return func2


func_ = func1(1)
func_()
