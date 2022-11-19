import os

"""
os.renames(old, new)：用于递归重命名目录或文件。
    old -- 要重命名的目录
    new --文件或目录的新名字。甚至可以是包含在目录中的文件，或者完整的目录树。
"""

old = 'D:\\window\\temp\\test.txt'
new = 'D:\\window\\temp\\test\\test2.txt'

# 重命名
os.renames(old, new)
