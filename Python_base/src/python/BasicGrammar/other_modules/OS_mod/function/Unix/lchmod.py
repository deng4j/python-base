import os
import stat

"""
os.lchmod(path, mode)：用于修改连接文件权限。Unix上可用。
    path -- 设置标记的文件路径
    mode -- 可以是以下一个或多个组成，多个使用 "|" 隔开：
        stat.S_ISUID:设置 UID 位
        stat.S_ISGID: 设置组 ID 位
        stat.S_ENFMT: 系统文件锁定的执法行动
        stat.S_ISVTX: 在执行之后保存文字和图片
        stat.S_IREAD: 对于拥有者读的权限
        stat.S_IWRITE: 对于拥有者写的权限
        stat.S_IEXEC: 对于拥有者执行的权限
        stat.S_IRWXU:对于拥有者读、写、执行的权限
        stat.S_IRUSR: 对于拥有者读的权限
        stat.S_IWUSR: 对于拥有者写的权限
        stat.S_IXUSR: 对于拥有者执行的权限
        stat.S_IRWXG: 对于同组的人读写执行的权限
        stat.S_IRGRP: 对于同组读的权限
        stat.S_IWGRP:对于同组写的权限
        stat.S_IXGRP: 对于同组执行的权限
        stat.S_IRWXO: 对于其他组读写执行的权限
        stat.S_IROTH: 对于其他组读的权限
        stat.S_IWOTH: 对于其他组写的权限
        stat.S_IXOTH:对于其他组执行的权限
"""

# 打开文件
path = "/var/www/html/foo.txt"
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# 关闭文件
os.close(fd)

# 修改文件权限，设置文件可以通过组执行
os.lchmod(path, stat.S_IXGRP)

# 设置文件可以被其他用户写入
os.lchmod("/tmp/foo.txt", stat.S_IWOTH)
