def func1(x):
    def func2():
        print("func2() - x：", x)

    return func2


func_ = func1(10)

print("------------------测试保存变量x----------------------")

func_()
