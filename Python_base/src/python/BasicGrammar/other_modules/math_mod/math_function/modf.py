import math

"""
modf( x ) 方法返回 x 的小数部分与整数部分，两部分的数值符号与 x 相同，整数部分以浮点型表示。
"""

print ("math.modf(100.12) : ", math.modf(100.12))
print ("math.modf(100.72) : ", math.modf(-100.72))
print ("math.modf(119) : ", math.modf(119))
print ("math.modf(math.pi) : ", math.modf(math.pi))
