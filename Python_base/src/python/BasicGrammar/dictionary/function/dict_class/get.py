"""
dict.get(key[, value])：返回指定键的值。
    key -- 字典中要查找的键。
    value -- 可选，如果指定键的值不存在时，返回该默认值。
"""

dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict1.get('Name')：{}".format(dict1.get('Name')))

print("dict1.get('XXXX',0)：{}".format(dict1.get('XXXX', 0)))
