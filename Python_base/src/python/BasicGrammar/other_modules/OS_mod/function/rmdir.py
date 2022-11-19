import os

"""
os.rmdir(path):用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。
"""


path = 'D:\\window\\temp\\test1\\test2'

# 删除路径
os.rmdir(path)
