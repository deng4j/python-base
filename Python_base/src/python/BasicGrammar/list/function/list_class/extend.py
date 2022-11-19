"""
extend(seq) 在列表末尾一次性追加另一个序列。
"""

print("------------------------- 追加list ------------------------------")
list1 = [1, '2', 2, 3]
list2 = [4, '5']

list1.extend(list2)  # 追加list
print(list1)
print(list2)

print("------------------------- 追加元组 ------------------------------")
list1 = [1, '2', 2, 3]
tuple1 = (4, '5')

list1.extend(tuple1)  # 追加元组
print(list1)
print(tuple1)

print("------------------------- 追加set集合 ------------------------------")
list1 = [1, '2', 2, 3]
set1 = {4, '5'}

list1.extend(set1)  # 追加set集合
print(list1)
print(set1)

print("------------------------- 追加字符串序列 ------------------------------")
list1 = [1, '2', 2, 3]
list1.extend('abc')
print(list1)

print("------------------------- 追加字典序列 ------------------------------")
list1 = [1, '2', 2, 3]
list1.extend({'name': '张三', 'age': 18})
print(list1)
