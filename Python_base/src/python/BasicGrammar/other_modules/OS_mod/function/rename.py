import os

"""
os.rename(src, dst)：用于命名文件或目录，从 src 到 dst,如果dst是一个存在的目录, 将抛出OSError。
    src -- 要修改的目录名
    dst -- 修改后的目录名
"""

src = 'D:\\window\\temp\\test.txt'
dst = 'D:\\window\\temp\\test2.txt'

# 重命名
os.rename(src, dst)
