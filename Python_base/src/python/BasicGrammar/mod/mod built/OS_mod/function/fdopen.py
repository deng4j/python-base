import os

"""
os.fdopen(fd, [, mode[, bufsize]])：用于通过文件描述符 fd 创建一个文件对象，并返回这个文件对象。该方法是内置函数 open() 的别名，
    可以接收一样的参数，唯一的区别是 fdopen() 的第一个参数必须是整型。
    
    fd -- 打开的文件的描述符，在Unix下，描述符是一个小整数。
    mode -- 可选，和 Python 内建的 open 函数一样，mode参数可以指定『r,w,a,r+,w+,a+,b』等，表示文件的是只读的还是可以读写的，
        以及打开文件是以二进制还是文本形式打开。这些参数和C语言中的<stdio.h>中fopen函数中指定的mode参数类似。
    bufsize -- 可选，指定返回的文件对象是否带缓冲：bufsize=0，表示没有带缓冲；bufsize=1，表示该文件对象是行缓冲的；bufsize=正数，
        表示使用一个指定大小的缓冲冲，单位为byte，但是这个大小不是精确的；bufsize=负数，表示使用一个系统默认大小的缓冲，
        对于tty字元设备一般是行缓冲，而对于其他文件则一般是全缓冲。如果这个参数没有制定，则使用系统默认的缓冲设定。
"""

path = 'D:\\window\\temp\\test.txt'

# 打开文件
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# 获取以上文件的对象
fo = os.fdopen(fd, "w+")

# 获取当前位置
print("Current I/O pointer position：".format(fo.tell()))

# 写入字符串
fo.write("Python is a great language.\nYeah its great!!\n")

# 读取内容
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("Read String is : ", str)

# 获取当前位置
print("Current I/O pointer position：".format(fo.tell()))

# 关闭文件
os.close(fd)
