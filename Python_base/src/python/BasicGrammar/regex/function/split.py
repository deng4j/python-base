import re

"""
re.split(pattern, str_class[, maxsplit=0, flags=0])：按照能够匹配的子串将字符串分割后返回列表
    pattern 匹配模式。
    str_class 待匹配的字符串。
    maxsplit：分割次数，maxsplit=1 分割一次，默认为 0，不限制次数。
    flags：标志位，用于控制正则表达式的匹配方式
"""

split = re.split('\W+', 'runoob, runoob, runoob.')
print(split)

split = re.split('a*', 'hello world')  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
print(split)
