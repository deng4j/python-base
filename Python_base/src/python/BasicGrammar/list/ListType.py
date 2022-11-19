import operator

"""
list = ['a', b,  c, 'd', e]
前索引： 0、 1、 2、 3、 4
后索引：-5、-4、-3、-2、-1
"""

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表

# 切片：list[start:end:step]，三个参数都是可选参数，start表示开始索引(默认0)，end表示结束索引（默认len,不包含len），step表示步长（默认1）

print("--------------------------- 切片 ----------------------------------")

print(list[0])  # 输出列表第一个元素
print(list[-1])  # 输出列表倒数第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[-4:-2])  # 从-4到-2
print(list[-1::-1])  # 从-1开始，每次索引减1
print(list[2:])  # 从索引2开始到结束

print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

print("--------------------------- 修改元素 ----------------------------------")
lst = [0, 1, 2, 3, 4, 5, 6, 7]
lst[4:6] = ['Morning']
print(lst)

print("-------------------------- 删除元素 -------------------------")

del list[1]  # 删除元素
print(list)

print("--------------- 自动解包1 ---------------")
list1 = [1, 2, 3]
a, b, c = list1
print("解包后：", a, b, c)

a, *b = list1  # 当变量少于元素个数时，b作为list接收后序所有元素
print("解包后：", a, b)

print("--------------- 自动解包2 ---------------")


def fun(p1, p2, p3):
    print("解包后：", p1, p2, p3)


fun(*[1, 2, 3])

print("--------------- 列表比较 ---------------")

a = [1, 2]
b = [2, 3]
print("operator.eq(a,b): ", operator.eq(a, b))
