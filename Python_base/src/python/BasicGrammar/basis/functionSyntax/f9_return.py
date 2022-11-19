print("------------------------ 当作函数的返回值 ------------------------")


def func15():
    print("----func15()----")


def func16(f):
    return f


func_ = func16(func15)
print(func_)
func_()
