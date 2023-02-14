"""
dict.setdefault(key, default=None)：setdefault() 方法和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
    key -- 查找的键值。
    default -- 键不存在时，设置的默认键值。
"""

dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict1获取'status'的值：{}".format(dict1.setdefault('status', 'Null')))
