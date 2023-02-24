import os

"""
os.path.splitdrive(path)：一般用在 windows 下，返回驱动器名和路径组成的元组
"""

path1 = 'D:\\window\\temp\\test.txt'

print(os.path.splitdrive(path1))
