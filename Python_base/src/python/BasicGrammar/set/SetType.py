"""
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

会去重

用可变类型创建集合set会抛异常，如list等
"""

sites = {'Google', 'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

sites.add("scdn")  # 添加元素
sites.update({1, 3})  # 添加元素
sites.remove(1)  # 移除，不存在会发生错误
sites.discard(8888)  # 移除,不存在会发生错误
print(sites)

print("-------------------------华丽分割线-------------------------")

try:
    set1 = {[1, 2], [3, 4]}
except:
    print("创建set错误：使用了可变对象做为元素")

print("-------------------------华丽分割线-------------------------")

print('Runoob' in sites)

print("-------------------------华丽分割线-------------------------")

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素

print("--------------- 自动解包1 ---------------")
set1 = {1, 2, 3}
a, b, c = set1
print("自动解包后：a={} b={} c={}".format(a, b, c))

print("--------------- 自动解包2 ---------------")
set1 = {1, 2, 3}
a, *b = set1  # 当变量少于元素个数时，b作为list接收后序所有元素
print("自动解包后：a={} b={}".format(a, b))

print("--------------- 自动解包3 ---------------")


def fun(p1, p2, p3):
    print("解包后：", p1, p2, p3)


fun(*{1, 2, 3})
