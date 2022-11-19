"""
__doc__：返回类的注释信息，无法被继承
"""


class Foo:
    'doc-doc'


print(Foo.__doc__)
