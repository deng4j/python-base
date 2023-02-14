"""
set.discard(value)：用于移除指定的集合元素。移除的元素不存在时不会抛异常。
"""

fruits = {"apple", "banana", "cherry"}

fruits.discard('apple')
fruits.discard('XXXX')

print(fruits)
