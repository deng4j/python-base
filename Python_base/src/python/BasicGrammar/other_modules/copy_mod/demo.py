import copy

"""
深拷贝：原对象与新对象不共享相同的属性
浅拷贝：它们具有相同的属性。
"""

lst = [[0], [1]]

print("lst对象id:", id(lst))
print("lst索引0元素id:", id(lst[0]))

print("---------------------- 浅拷贝 -----------------------")
lst1 = lst.copy()  # 浅拷贝

print("lst1对象id:", id(lst1))
print("lst1索引0元素id:", id(lst1[0]))

print("---------------------- 深拷贝 -----------------------")

lst2 = copy.deepcopy(lst)  # 深拷贝

print("lst2对象id:", id(lst2))
print("lst2索引0元素id:", id(lst2[0]))
