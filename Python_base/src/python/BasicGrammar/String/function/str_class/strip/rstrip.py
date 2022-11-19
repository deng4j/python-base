"""
str.rstrip([chars])：删除末尾指定字符串（默认为空白符）。
"""

str1 = 'aaabbbccc???'

print(str1.rstrip('?'))
print(str1.rstrip('a'))

print("---------------------------------------")

str1 = 'abababKKKccc???'

print(str1.rstrip('??'))
