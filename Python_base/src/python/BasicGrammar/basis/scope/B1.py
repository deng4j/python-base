"""
测试pycharm的编译检查：
    测试1：pycharm是否可以确定一个函数的返回值。

结论：pycharm只是做了可能性判断。
"""


def getQueue():
    print('getQueue')


class Foo:

    def __init__(self):
        self.myqueue = getQueue()

    def getLen(self):
        print("foo getLen")


foo = Foo()
db = foo.myqueue.getLen()  # 测试1，不确定函数的返回值，只会将库中存在.getLen()函数清空呈现出来。
