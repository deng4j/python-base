import os

"""
os.path.commonprefix(list)：返回list(多个路径)中，所有path共有的最长的路径
"""

path = 'D:\\window\\temp\\test.txt'
path1 = 'D:\\window\\temp\\testPath\\t.txt'
path2 = 'D:\\window\\aaa'

lst = [path, path1, path2]

print(os.path.commonprefix(lst))
