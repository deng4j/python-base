from contextlib import contextmanager

"""
Python 还提供了⼀个 contextmanager 的装饰器，更进⼀步简化了上下⽂管理器的实现⽅式。
    通过 yield 将函数分割成两部分，yield 之前的语句在 __enter__ ⽅法中执⾏，
    yield 之后的语句在 __exit__ ⽅法中执⾏。紧跟在 yield 后⾯的值是函数的返回值。
"""


@contextmanager
def my_open(path, mode):
    print("open...")
    f = open(path, mode)
    yield f
    print("close...")
    f.close()


with my_open('out.txt', 'w') as f:
    f.write("hello , the simplest context manager")
