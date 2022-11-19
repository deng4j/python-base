import os

"""
os.path.samestat(stat1, stat2)：判断stat tuple stat1和stat2是否指向同一个文件
"""

path1 = 'D:\\window\\temp\\test.txt'
path2 = 'D:\\window\\temp\\test.txt'

stat1 = os.stat(path1)
stat2 = os.stat(path2)

print(os.path.samestat(stat1, stat2))
