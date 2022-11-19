import os

"""
os.fpathconf(fd, name)：用于返回一个打开的文件的系统配置信息。Unix 平台下可用。
    fd -- 文件描述符
    name -- 检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中
        指定（POSIX.1, Unix 95, Unix 98, 和其它）。一些平台也定义了一些额外的名字。
        这些名字在主操作系统上pathconf_names的字典中。对于不在pathconf_names中的配置变量，
        传递一个数字作为名字，也是可以接受的。
"""

# 打开文件
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

print("%s" % os.pathconf_names)

# 获取文件最大连接数
no = os.fpathconf(fd, 'PC_LINK_MAX')
print("Maximum number of links to the file. :%d" % no)

# 获取文件名最大长度
no = os.fpathconf(fd, 'PC_NAME_MAX')
print("Maximum length of a filename :%d" % no)

# 关闭文件
os.close(fd)
