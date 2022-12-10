"""
可变参数：
    1. 如果在函数调用时没有指定参数，它就是一个空元组。
    2. 可变参数 *vartuple：加了星号 * 的参数会以元组(tuple)的形式"导入"，存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组。
    3. 关键字参数 **vardict：加了两个星号 ** 的参数会以字典的形式"导入"。
    4. 声明函数时，参数中星号 * 可以单独出现，如果单独出现星号 *，则星号 * 后的参数必须用关键字传入
"""

print("------------ *vartuple ------------")


def vartuple(arg1, *vartuple):
    print("固参arg1:{}  变参vartuple:{}  vartuple类型:{}".format(arg1, vartuple, type(vartuple)))


vartuple(70, 60, 50)
vartuple(10)

print("------------ **vardict ------------")


def vardict(arg1, **vardict):
    print("固参arg1:{}  变参vardict:{}  vardict类型:{}".format(arg1, vardict, type(vardict)))


vardict(1, a=2, b=3)

print("------------ * ------------")


def f7(a, b, *, c):
    return a + b + c


print(f7(1, 2, c=3))
