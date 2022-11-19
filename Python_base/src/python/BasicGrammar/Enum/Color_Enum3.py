from enum import Enum, unique

"""
@unique装饰器，枚举中出现相同value的成员会抛异常
"""


@unique
class Color(Enum):
    RED = 1
    GREEN = 1
    BLUE = 3
