"""
groupby：对列表中的元素进行分组
"""
from pipe import groupby, select

nested = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lst = nested | groupby(lambda x: 'even' if x % 2 == 0 else 'odd') | select(lambda x: {x[0]: list(x[1])})
print(list(lst))
