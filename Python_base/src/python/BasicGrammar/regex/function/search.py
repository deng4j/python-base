import re

"""
re.search(pattern, str_class, flags=0)：扫描整个字符串并返回第一个成功的匹配。
"""

print(re.search('www', 'www.runoob.com').span())
print(re.search('com', 'www.runoob.com').span())

search = re.search('xxx', 'www.runoob.com')
if search is None:
    print("匹配失败")
else:
    search.span()
