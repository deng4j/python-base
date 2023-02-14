"""
str.replace(old, new[, max])：替换字符串。
    old -- 将被替换的子字符串。
    new -- 新字符串，用于替换old子字符串。
    max -- 可选字符串, 替换不超过 max 次
"""

str1 = 'aaaaaaabbbccc???'
print(str1.replace('a', 'x', 3))
