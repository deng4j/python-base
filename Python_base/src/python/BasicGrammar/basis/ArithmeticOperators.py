print("------------ Python算术运算符 ------------")

print("1+1的值为：", 1 + 1)

print("减法4-2值为：", 4 - 2)

print("乘法2*3值为：", 2 * 3)

print("除法5/3值为：", 5 / 3)

print("5%2取模值为：", 5 % 2)

print("幂 - 返回x的y次幂：", 2 ** 3)

print("取整除 - 向下取接近商的整数：", 10 // 3)

print("------------ Python比较运算符 ------------")

print("1 等于 1", 1 == 1)

print("2  不等于 3", 2 != 3)

print("3 小于 5", 3 < 5)

print("4 大于 2", 4 > 2)

print("5小于等于20", 5 <= 20)

print("6大于等于2", 6 >= 2)

print("2 <= 6 <= 8：", 2 <= 6 <= 8)

print("------------ Python赋值运算符 ------------")
"""
python语言中替换自增和自减，因为python中的数字类型是不可变数据
数字类型数据在【内存】中是不会发生改变，当变量值发生改变时，会新申请一块内存赋值为新值，然后将变量指向新的内存地址。
整数池中，在[-5, 256]范围内，值相同的变量都指向了同一内存地址。
"""
a = 0
a = 21 + 10
print(a)

b = 3
b += 10
print(b)

c = 2
c *= 10
print(c)

d = 121
d /= 10
print(d)

e = 5
e %= 2
print(e)

f = 3
f **= 2
print("幂赋值运算符：", f)

g = 111
g //= 10
print("取整除赋值运算符：", g)

"""
:= 海象运算符，可在表达式内部为变量赋值。
海象运算符本质上就是一个“赋值表达式”，一边完成赋值工作，一边返回刚刚赋值完的变量。
"""
if (n := 2) > 1:
    print(n)

print("------------ Python赋值运算符 ------------")
"""
and == &&
or  == ||
not == !
"""

print("2>3 and 1/0>5：", 2 > 3 and 1 / 0 > 5)
print("3>2 or 1/0>5：", 3 > 2 or 1 / 0 > 5)

print("------------ Python成员运算符 ------------")
"""
in：如果在指定的序列中找到值返回 True，否则返回 False。
not in：如果在指定的序列中没有找到值返回 True，否则返回 False。
"""

list = [1, 2, 3, 4, 5]
print("2 在给定的列表中 list 中：", 2 in list)
print("8 不在给定的列表中 list 中：", 8 not in list)

print("------------ Python身份运算符 ------------")
"""
is： 是判断两个标识符是不是引用自一个对象
is not：是判断两个标识符是不是引用自不同对象

is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
"""
a = 10
b = 10
print("a 和 b 有相同的标识：", a is b)
print("1 和 1 有相同的标识：", 1 is 1)
print("a 和 1 有相同的标识：", a is 1)

print("a is None：", a is None)
