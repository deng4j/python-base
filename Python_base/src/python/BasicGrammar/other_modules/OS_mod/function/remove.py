import os

"""
os.remove(path) 方法用于删除指定路径的文件。如果指定的路径是一个目录，将抛出OSError。在Unix, Windows中有效
"""

path = 'D:\\window\\temp\\test.txt'

os.remove(path)
