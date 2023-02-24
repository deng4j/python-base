"""
Pipe模块：管道(|) 将一种方法的结果传递给另一个方法。

注意：
    1.返回的对象取决于最后一个管道的返回值。如data｜where｜select，返回的是map

自定义流处理函数：需要定义一个生成器函数并加上修饰器Pipe。
"""
from pipe import Pipe, where


@Pipe
def take_x(iterable, predicate):
    for idx, x in enumerate(iterable):
        if predicate(idx):
            yield x
        else:
            return


lst = list([1, 1, 2, 3, 5, 8, 13, 21, 34] | where(lambda x: x % 2 == 0))
print(lst)
