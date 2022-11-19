"""
copy() 函数返回一个字典的浅复制。

问题：跑items.py前居然运行了copy.py的代码，故改名copy_test.py
"""

dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict2 = dict1.copy()

print("dict1['Name']：{}".format(id(dict1['Name'])))
print("dict2['Name']：{}".format(id(dict2['Name'])))
