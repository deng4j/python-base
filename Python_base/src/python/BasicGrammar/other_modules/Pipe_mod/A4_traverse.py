"""
traverse：递归展开可迭代对象
"""
from pipe import traverse

nested = [[1, [2, 3]], 'abc', [5, 6]]

lst = list(nested | traverse)
print(lst)
