"""
Python变量的作用域一共有4种：
    L （Local） 局部作用域
    E （Enclosing） 闭包函数外的函数中
    G （Global） 全局作用域
    B （Built-in） 内建作用域 以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
"""

# 全局变量
x = 5
y = 1


def func1():
    x = 10  # 局部变量
    print(x)


def func2(y):  # 局部变量
    y = 2
    print(y)


func1()
print(x)

func2(3)
print(y)
