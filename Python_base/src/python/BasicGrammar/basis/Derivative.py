"""
Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。

Python 支持各种数据结构的推导式：
    列表(list)推导式：new_list = [expression for_loop_expression if condition]
    字典(dict)推导式：new_dict ={ key_expr: value_expr for_loop_expression if condition }
    集合(set)推导式：new_set = { expr for_loop_expression if condition }
    生成器推导式：生成器推导式和列表推导式的用法也完全相同，只是元组推导式是用 () 圆括号将各部分括起来，
        而列表推导式用的是中括号 []，另外元组推导式返回的结果是一个生成器对象。
        new_list = （expression for_loop_expression if condition）
"""

print("--------------------列表推导式---------------------------")
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

print("--------------------字典推导式---------------------------")
listdemo = ['Google', 'Runoob', 'Taobao']
newdict = {key: len(key) for key in listdemo}
print(newdict)

print("--------------------集合推导式---------------------------")
abc = {x for x in 'abracadabra' if x not in 'abc'}
print(abc)

print("--------------------元组推导式（生成器表达式---------------------------")
dic = {'a': 1, 'b': 2, 'c': 3}
ndic = ((k, v) for k, v in dic.items() if v > 1)
print(ndic)
print(tuple(ndic))  # 使用 tuple() 函数，可以直接将生成器对象转换成元组

print("--------------------推导式嵌套---------------------------")
lst = [[1, 2, 4, 6], [4, 2, 5, 1]]

lst = [j for i in lst for j in i]
print(lst)

lst = [j for j in (i for i in lst)]
print(lst)

lst = [(x, y) for x in [1, 2, 3] for y in [3, 4, 5]]
print(lst)
