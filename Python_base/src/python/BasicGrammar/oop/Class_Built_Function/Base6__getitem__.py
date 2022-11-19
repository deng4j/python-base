"""
__getitem__：对象[]获取值时触发
"""


class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        print('getitem执行：', item)
        value = self.__dict__[item]
        return value


foo = Foo("sb", 181)

print(foo['age'])

print("---------------------------------------")


class Boo:

    def __init__(self) -> None:
        self.data = [[1, 2], [3, 4]]

    def __getitem__(self, item):
        print(item)
        return self.data[item[0]]


boo = Boo()
print(boo[1, 2])  # 传递一个元组
