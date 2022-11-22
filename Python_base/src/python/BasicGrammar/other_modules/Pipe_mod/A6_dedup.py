"""
dedup：去重
"""
from pipe import dedup

nested = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]

obj = nested | dedup
print(obj)
print(list(obj))

obj = nested | dedup(lambda key: key < 5)
print(list(obj))
