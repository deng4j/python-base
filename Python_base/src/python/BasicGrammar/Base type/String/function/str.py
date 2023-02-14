"""
 str(obj)：构造函数，将obj转化为字符串
"""

n1 = str(10)
print(type(n1))
print(n1 + "str")

dict1 = {'name': '张三', 'age': 18}
print("dict转str", str(dict1))

print("set转str", str({1, 2, 3}))

print("tuple转str", str((1, 2, 3)))

list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
print("list转str", str(list1))
