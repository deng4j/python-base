"""
 str(obj)：构造函数，将obj转化为字符串
"""

n1 = str(10)
print(type(n1))
print(n1 + "str")

dict1 = {'name': '张三', 'age': 18}
print("str转dict", str(dict1))

print("str转set", str({1, 2, 3}))

print("str转tuple", str((1, 2, 3)))

list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
print("str转list", str(list1))
