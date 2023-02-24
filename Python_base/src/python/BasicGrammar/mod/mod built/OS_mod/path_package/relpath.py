import os

"""
os.path.relpath(path[, start])：用于从当前工作目录或给定目录获取到给定路径的相对文件路径。
"""

path = 'D:\\window\\temp\\test.txt'
start = 'D:\\window\\t\\test.txt'

print(os.path.relpath(path, start))
