"""
dict.keys()：返回所有key。是一个动态视图，不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。
"""

dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict1所有键：{}".format(dict1.keys()))

print("------------------------- 测获取keys是为动态变化的 ------------------------------")

keys = dict1.keys()

del dict1['Name']
print(keys)
