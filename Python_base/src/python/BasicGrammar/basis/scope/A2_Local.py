# 全局变量
x = 5
y = 1


def func1():
    global x  # 显示地告诉解释器 x 为全局变量，去全局作用域中寻找
    x = x + 1
    print(x)


def func2():
    y = 0
    print(y)


func1()
print(x)

func2()
print(y)
