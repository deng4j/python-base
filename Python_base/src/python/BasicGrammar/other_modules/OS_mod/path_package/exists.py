import os

"""
os.path.exists(path):路径存在则返回True,路径损坏返回False
"""

path = 'D:\\window\\temp\\test.txt'
path1 = 'D:\\window\\temp\\tesaaat.txt'

print(os.path.exists(path))
print(os.path.exists(path1))
