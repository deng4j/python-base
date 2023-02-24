"""
Where：可迭代对象中的过滤元素
"""
from pipe import where

arr = [1, 2, 3, 4, 5]

whe = arr | where(lambda x: x % 2 == 0)
print(whe)

lst = list(whe)
print(lst)
