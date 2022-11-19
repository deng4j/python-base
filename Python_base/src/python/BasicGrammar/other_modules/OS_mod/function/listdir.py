import os

"""
os.listdir(path)：用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 . 和 .. 即使它在文件夹中。只支持在 Unix, Windows 下使用。
"""

path = 'D:\\window\\temp\\'

dirs = os.listdir(path)

# 输出所有文件和文件夹
for file in dirs:
    print(file)
