"""
构造函数dict()：可以直接从键值对序列中构建字典
    class dict(**kwarg)
    class dict(mapping, **kwarg)
    class dict(iterable, **kwarg)
        **kwargs -- 关键字。
        mapping -- 元素的容器，映射类型（Mapping Types）是一种关联式的容器类型，它存储了对象与对象之间的映射关系。
        iterable -- 可迭代对象。
"""

dict2 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])  # 可迭代对象方式来构造字典
print(dict2)

d = dict(a='a', b='b', t='t')
print(d)

numbers1 = dict({'x': 4, 'y': 5})
print('numbers1 =', numbers1)

numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =', numbers2)

numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =', numbers3)

# zip() 创建可迭代对象
numbers4 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
print('numbers4 =', numbers4)
