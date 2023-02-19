import os

"""
os.path.lexists(path):路径存在则返回True,路径损坏返回False
"""

path = 'D:\\window\\temp\\test.txt'
path1 = 'D:\\window\\temp\\tesaaat.txt'

print(os.path.lexists(path))

print(os.path.lexists(path1))
