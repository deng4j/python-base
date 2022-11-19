"""
dict.values()：返回所有value。是一个动态视图，不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。
"""

dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict1所有value：{}".format(dict1.values()))

print("------------------------- 测获取values是为动态变化的 ------------------------------")

values = dict1.values()

del dict1['Name']
print(values)
