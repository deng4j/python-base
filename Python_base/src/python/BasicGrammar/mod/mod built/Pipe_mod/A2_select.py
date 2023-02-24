"""
select：将函数应用于可迭代对象
"""
from pipe import select

arr = [1, 2, 3, 4, 5]

sel = arr | select(lambda x: x * 2)
print(sel)  # 返回一个map对象

lst = list(sel)
print(lst)

lst = list(arr | select(lambda x: x + 1) | select(lambda x: x * 2))
print(lst)
