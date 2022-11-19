"""
pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。
    key - 要删除的键
    default - 当键 key 不存在时返回的值
"""

dict1 = {'a': '张三', 'b': 18, 'c': '001'}

print(dict1.pop('a'))
print(dict1.pop('z', 3))
print(dict1.pop('z'))
