"""
构造方法参数探索
"""

class A:
    def __init__(self, pa=(0.1, 1.0, 10.0), ):
        print('pa：', pa)


class B:
    def __init__(self, pb=(0.1, 1.0, 10.0), ):
        print('pb：', pb)


class C:
    pass


class D(A, B):
    """
    不重写构造，继承A的构造
    """
    pass


class E(C, A):
    """
    不重写构造，C只有默认构造，E继承A的构造
    """
    pass


d1 = D(pa=(1, 2, 3,))
try:
    d2 = D(pb=(1, 2, 3,))
except Exception as e:
    print('error：', e.args)

e1 = E(pa=(1, 3, 5))
