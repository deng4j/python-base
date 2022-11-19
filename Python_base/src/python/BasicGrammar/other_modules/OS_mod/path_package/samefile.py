import os

"""
os.path.samefile(path1, path2)：判断目录或文件是否相同
"""

path = 'D:\\window\\temp\\test.txt'
path1 = 'D:\\window\\temp\\foo.txt'

print(os.path.samefile(path, path1))
