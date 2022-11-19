"""
__repr__：
    1.str函数或者print函数--->obj.__str__()
    2.repr或者交互式解释器--->obj.__repr__()
"""


class School:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def __repr__(self):
        return 'School(%s,%s)' % (self.name, self.addr)


s1 = School('UGUGK', '北京朝阳区')
print('from repr: ', repr(s1))
