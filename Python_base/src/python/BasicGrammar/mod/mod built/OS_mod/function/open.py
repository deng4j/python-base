import os

"""
os.open(file, flags[, mode]):用于打开一个文件，并且设置需要的打开选项，模式参数mode参数是可选的，默认为 0777。
    file -- 要打开的文件
    flags -- 该参数可以是以下选项，多个使用 "|" 隔开：
        os.O_RDONLY: 以只读的方式打开
        os.O_WRONLY: 以只写的方式打开
        os.O_RDWR : 以读写的方式打开
        os.O_NONBLOCK: 打开时不阻塞
        os.O_APPEND: 以追加的方式打开
        os.O_CREAT: 创建并打开一个新文件
        os.O_TRUNC: 打开一个文件并截断它的长度为零（必须有写权限）
        os.O_EXCL: 如果指定的文件存在，返回错误
        os.O_SHLOCK: 自动获取共享锁
        os.O_EXLOCK: 自动获取独立锁
        os.O_DIRECT: 消除或减少缓存效果
        os.O_FSYNC : 同步写入
        os.O_NOFOLLOW: 不追踪软链接
"""

path = 'D:\\window\\temp\\test.txt'

# 打开文件
fd = os.open(path, os.O_RDWR | os.O_CREAT)

#  写入字符串
os.write(fd, "This is test".encode("utf-8"))

# 关闭文件
os.close(fd)
