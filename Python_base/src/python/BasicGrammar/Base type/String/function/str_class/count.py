"""
count(sub, start= 0,end=len(str_class)) 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
"""

str = "www.runoob.com"
sub = 'o'
print("str.count('o') : ", str.count(sub))

sub = 'run'
print("str.count('run', 0, 10) : ", str.count(sub, 0, 10))
