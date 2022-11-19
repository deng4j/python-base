"""
当在内存中创建类对象Foo时, python会在类的定义中寻找__metaclass__属性, 如果找到了, python就用它来创建Foo, 如果没有找到,
    就会去父类找。都没找到就会用内建的type元类来创建这个类.

python2有效
"""


class UpperAttrMetaClass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attrs = dict((name.upper(), value) for name, value in attrs)  # 转大写

        # return type.__new__(cls, name, bases, uppercase_attrs)
        return super(UpperAttrMetaClass, cls).__new__(cls, name, bases, uppercase_attrs)


class Foo(object):
    # python2有效
    __metaclass__ = UpperAttrMetaClass
    bar = 'bip'


# python3使用
class Boo(metaclass=UpperAttrMetaClass):
    bar = 'bip'


if __name__ == '__main__':
    print(Foo.__dict__)
    print(Boo.__dict__)
