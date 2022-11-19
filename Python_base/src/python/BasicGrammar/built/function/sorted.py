"""
sorted(iterable, key=None, reverse=False)：对所有可迭代的对象进行排序操作。返回一个新的可迭代对象。
    iterable -- 可迭代对象。
    key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
"""

lst = [5, 2, 3, 1, 4]
sorted_lst = sorted(lst)
print(sorted_lst)

print(id(lst))
print(id(sorted_lst))

print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))

example_list = [5, 0, 6, 1, 2, 7, 3, 4]
print(sorted(example_list, key=lambda x: x * -1))
