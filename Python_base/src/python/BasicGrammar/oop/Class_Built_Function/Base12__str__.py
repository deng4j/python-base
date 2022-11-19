"""
__str__：打印时触发
"""


class People:
    pass


p = People()
print(p)


class Book:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}---{self.age}'  # 如果不返回字符串类型，则会报错


book = Book("张三", 18)
print(book.__str__())
