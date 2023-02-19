"""
chain：使用chain来链接一系列可迭代对象。
"""
from pipe import chain

nested = [1, [2, 3]], 'abc', [5, 6]

lst = list(nested | chain)
print(lst)
