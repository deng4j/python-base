from collections import Iterable

"""
迭代器：⼀个类实现了 __iter__ ⽅法和 __next__ ⽅法的对象，就是⾃定义迭代器。

当调⽤iter(迭代器对象)时，会调⽤对象的 __iter__() ⽅法
当调⽤next(迭代器对象)时，会调⽤对象的 __next__() ⽅法
迭代器⾃身正是⼀个迭代器，所以迭代器的 __iter__ ⽅法返回⾃身即可。
"""


class Foo:
    def __init__(self, start, stop):
        self.num = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= self.stop:
            raise StopIteration
        n = self.num
        self.num += 1
        return n


f = Foo(0, 10)
for i in f:
    print(i)

print(isinstance(f, Iterable))  # 判断是否为一个可迭代对象
print(isinstance('abcd', Iterable))  # 判断是否为一个可迭代对象
