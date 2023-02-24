import os

"""
os.fpathconf(fd, name)：用于返回一个打开的文件的系统配置信息。Unix上可用。
    fd -- 打开的文件的描述符。
    name -- 可选，和buffersize参数和Python内建的open函数一样，mode参数可以指定『r,w,a,r+,w+,a+,b』等，表示文件的是只读的
        还是可以读写的，以及打开文件是以二进制还是文本形式打开。这些参数和C语言中的<stdio.h>中fopen函数中指定的mode参数类似。
"""

# 打开文件
fd = os.open("/tmp/foo.txt", os.O_RDWR | os.O_CREAT)

print("pathconf_names:", os.pathconf_names)

# 获取最大文件连接数
no = os.fpathconf(fd, 'PC_LINK_MAX')
print("文件最大连接数为 :{}".format(no))

os.close(fd)
