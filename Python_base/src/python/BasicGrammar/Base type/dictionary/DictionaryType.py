"""
字典是无序的对象集合。字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
注意：键(key)必须使用不可变类型，如不能使用list作为key。
在同一个字典中，键(key)是唯一的，相同的key，后面的会覆盖前面的。
"""

dict1 = {}
print(type(dict1))

dict1['one'] = "1 - 菜鸟教程"
dict1[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob1', 'name': 'runoob2', 'code': 1, 'site': 'www.runoob.com'}

print(tinydict)  # 输出完整的字典
print(dict1['one'])  # 输出键为 'one' 的值，没有该key会抛异常
print(dict1[2])  # 输出键为 2 的值
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
print(tinydict.get("site"))  # 通过key获取value，字典中没有会返回None
print('name' in tinydict)

print("-------------------------字典元素操作-------------------------")
tinydict['name'] = "张三"  # 修改
tinydict['age'] = "18"  # 新增
del tinydict['code']  # 删除元素
print(tinydict)

print("-------------------------华丽分割线-------------------------")

print(dict(Runoob=1, Google=2, Taobao=3))

print("-------------------------华丽分割线-------------------------")

dict3 = {x: x ** 2 for x in (2, 4, 6)}
print(dict3)

print("--------------- 自动解包 ---------------")

dic = {"name": "张三", "age": 18, "number": "001"}

a, b, c = dic  # 仅将key传递给变量
print("解包后：", a, b, c)

a, *b = dic  # 当变量少于元素个数时，b作为list接收后序所有元素
print("解包后：", a, b)

print("--------------- 自动解包 * ---------------")


def unpacking(a, b, c):
    print("解包后：", a, b, c)


dic = {"a": "张三", "b": 18, "c": "001"}
unpacking(*dic)  # 单*号，把键名传递，键数和形参数一样
unpacking(**dic)  # 双*号，把键的值传递，键名和形参数一样

print("--------------- 作为参数传递 ---------------")


def work(dic):
    print(dic)


dic = {"a": "张三", "b": 18, "c": "001"}

work(dic)

print("--------------- 删除字典 ---------------")

del tinydict  # 'tinydict' is not defined

print("--------------- 循环1 ---------------")

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for k in dict1:
    print("{}  {}".format(k, dict1[k]))

print("--------------- 循环2 ---------------")

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for k, v in dict1.items():
    print("{}  {}".format(k, v))
