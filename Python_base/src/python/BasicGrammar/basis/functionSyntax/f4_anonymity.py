"""
Python 使用 lambda 来创建匿名函数:
    lambda 只是一个表达式，函数体比 def 简单很多。
    lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
    lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
    虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
    我们可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。
"""

f8 = lambda a: a + 10
print(f8(10))

sum = lambda arg1, arg2: arg1 + arg2
print("相加后的值为 : ", sum(10, 20))


def func9(n):
    return lambda a: a * n


f10 = func9(2)
f11 = func9(3)
print(f10(11))
print(f11(11))
