import os

"""
os.removedirs(path) 用于递归删除目录。像rmdir(), 如果子文件夹成功删除, removedirs()才尝试它们的父文件夹，
    直到抛出一个error(它基本上被忽略,因为它一般意味着你文件夹不为空)。
"""

path = 'D:\\window\\temp\\test\\testPopen'

os.removedirs(path)
