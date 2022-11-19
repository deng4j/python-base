"""
class property([fget[, fset[, fdel[, doc]]]])：在新式类中返回属性值。
    fget -- 获取属性值的函数
    fset -- 设置属性值的函数
    fdel -- 删除属性值函数
    doc -- 属性描述信息
"""


class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        print("getx()")
        return self._x

    def setx(self, value):
        print("setx()")
        self._x = value

    def delx(self):
        print("delx()")
        del self._x

    x = property(getx, setx, delx, "doc")


c = C()
c.x  # 将触发 getter
c.x = 'xxxx'  # 将触发 getter
del c.x  # 触发 deleter
