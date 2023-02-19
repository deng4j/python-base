import os

"""
os.link(src, dst)：os.link() 方法用于创建硬链接，名为参数 dst，指向参数 src。
    该方法对于创建一个已存在文件的拷贝是非常有用的。只支持在 Unix, Windows 下使用。
    
    src -- 用于创建硬连接的源地址
    dst -- 用于创建硬连接的目标地址
"""

path = 'D:\\window\\temp\\test.txt'

# 打开文件
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# 关闭文件
os.close(fd)

# 创建以上文件的拷贝
dst = "D:\\window\\temp\\foo.txt"
os.link(path, dst)
