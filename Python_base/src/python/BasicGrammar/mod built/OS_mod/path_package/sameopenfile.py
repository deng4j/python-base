import os

"""
os.path.sameopenfile(fp1, fp2)：判断fp1和fp2是否指向同一文件
"""

path1 = 'D:\\window\\temp\\test.txt'
path2 = 'D:\\window\\temp\\test.txt'

file1 = open(path1, mode='r')
file2 = open(path2, mode='r')

fd1 = file1.fileno()
fd2 = file2.fileno()

print(os.path.sameopenfile(fd1, fd2))
