import re

"""
match 和 search 是匹配一次 findall 匹配所有。

re.findall(pattern, str_class, flags=0)或pattern.findall(str_class[, pos[, endpos]])：
    在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，
    如果没有找到匹配的，则返回空列表。

    pattern 匹配模式。
    str_class 待匹配的字符串。
    pos 可选参数，指定字符串的起始位置，默认为 0。
    endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
"""

print("---------------- 查找字符串中的所有数字 -------------------")

result1 = re.findall(r'\d+', 'runoob 123 google 456')

pattern = re.compile(r'\d+')  # 查找数字
result2 = pattern.findall('runoob 123 google 456')
result3 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)
print(result3)

print("---------------- 多个匹配模式，返回元组列表 -------------------")

result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(result)