"""
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

元组索引与字符串相似
"""
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组
print(123 in tinytuple)

print("------------------ 定义元组 -----------------")

tuple1 = 'aaa', 404
print(type(tuple1))
print(tuple1)

print("----------- 迭代 -------------")
for x in tuple:
    print(x)

print("--------------- 自动解包 ---------------")
tuple1 = (1, 2, 3)
a, b, c = tuple1
print("解包后：", a, b, c)

print("--------------- 自动解包2 ---------------")
tup2 = (1, 2, 3)
a, *b = tup2  # 当变量少于元素个数时，b作为list接收后序所有元素
print("自动解包后：a={} b={}".format(a, b))

print("--------------- 自动解包2 ---------------")


def fun(a, b, c):
    print("{}  {}  {}".format(a, b, c))


fun(*tup2)

print("--------------- 删除元组 ---------------")
tup1 = (12, 34.56)
del tup1
try:
    print(tup1)
except NameError as e:
    print(e)
