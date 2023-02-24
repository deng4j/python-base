import os

"""
dirname() 函数从完整路径中得到目录。
"""

path = '/file/folder1/textIO.txt'

# 获取文件的路径
print(os.path.dirname(path))

# 获取本文件所在目录
print(os.path.dirname(os.path.abspath(__file__)))