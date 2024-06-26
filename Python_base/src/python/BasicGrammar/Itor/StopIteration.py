print("------------ StopIteration -------------")
"""
StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中
我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
"""


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
