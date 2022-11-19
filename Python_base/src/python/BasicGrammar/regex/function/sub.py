import re

"""
re.sub(pattern, repl, str_class, count=0, flags=0)用于替换字符串中的匹配项：
    pattern : 正则中的模式字符串。
    repl : 替换的字符串，也可为一个函数。
    str_class : 要被查找替换的原始字符串。
    count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
    flags : 编译时用的匹配模式，数字形式。
"""

print("---------------- sub ---------------")

phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)

print("---------------- repl 参数是一个函数 ---------------")


def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
