import os

"""
os.lchflags(path, flags)：用于设置路径的标记为数字标记，类似 chflags()，但是没有软链接。Unix上可用。
    path -- 设置标记的文件路径
    flags -- 可以由一个或多个标记组合，多个使用"|"隔开：
        UF_NODUMP: 非转储文件
        UF_IMMUTABLE: 文件是只读的
        UF_APPEND: 文件只能追加内容
        UF_NOUNLINK: 文件不可删除
        UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
        SF_ARCHIVED: 可存档文件(超级用户可设)
        SF_IMMUTABLE: 文件是只读的(超级用户可设)
        SF_APPEND: 文件只能追加内容(超级用户可设)
        SF_NOUNLINK: 文件不可删除(超级用户可设)
        SF_SNAPSHOT: 快照文件(超级用户可设)
"""

# 打开文件
path = "/var/www/html/foo.txt"
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# 关闭文件
os.close(fd)

# 修改文件标记
os.lchflags(path, os.UF_IMMUTABLE)
