"""
str.lstrip([chars])：删除开头指定字符串（默认为空白符）。
"""

str1 = 'aaabbbccc???'

print(str1.lstrip('b'))
print(str1.lstrip('a'))

print("---------------------------------------")

str1 = 'abababKKKccc???'

print(str1.lstrip('ab'))
