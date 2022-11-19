import re

"""
re.finditer(pattern, str_class, flags=0)：在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
    pattern：匹配的正则表达式
    str_class：要匹配的字符串。
    flags：标志位，用于控制正则表达式的匹配方式。
"""

it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())
