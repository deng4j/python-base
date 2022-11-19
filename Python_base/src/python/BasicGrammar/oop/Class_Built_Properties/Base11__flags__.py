"""
__flags__, 返回一串数字，用来判断该类型能否被序列化（if it's a heap type), __flags__ & 512
"""


class Aoo:
    a = None
    b = 13
    c = 'a'
    d = 14


print(Aoo.__flags__)
