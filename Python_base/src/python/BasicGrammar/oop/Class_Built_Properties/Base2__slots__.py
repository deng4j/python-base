"""
__slots__：是一个类变量，变量值可以是列表，元祖，或者可迭代对象，也可以是一个字符串(意味着所有实例只有一个数据属性)。

作用：字典会占用大量内存，如果你有一个属性很少的类，但是有很多实例，为了节省内存可以使用__slots__取代实例的__dict__。

缺点：不能再给实例添加新的属性了。
"""


class Foo:
    __slots__ = 'x'


foo = Foo()
foo.x = 10
print(foo.x)

try:
    foo.y = 20
except AttributeError as e:
    print(e)

try:
    print(foo.__dict__)
except AttributeError as e:
    print(e)

print(foo.__slots__)

print("---------------------------------------------------")


class Book:
    __slots__ = ['a', 'b']


book = Book()
book.a = 20
print(book.a)
print(book.__slots__)
