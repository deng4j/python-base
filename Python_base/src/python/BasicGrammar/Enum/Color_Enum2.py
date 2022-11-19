from enum import Enum

"""
枚举类中各个成员必须保证 name 互不相同，但 value 可以相同
"""


class Color(Enum):
    RED = 1
    GREEN = 1
    BLUE = 3


# 相同value的成员，排在后面的成员GREEN会被当作RED的别名
print("Color['GREEN']:", Color['GREEN'])
