import os, stat

"""
os.chflags(path, flags)：设置路径的标记为数字标记。多个标记可以使用 OR 来组合起来。只支持在 Unix 下使用。
    path -- 文件名路径或目录路径。
    flags -- 可以是以下值：
        stat.UF_NODUMP: 非转储文件
        stat.UF_IMMUTABLE: 文件是只读的
        stat.UF_APPEND: 文件只能追加内容
        stat.UF_NOUNLINK: 文件不可删除
        stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
        stat.SF_ARCHIVED: 可存档文件(超级用户可设)
        stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
        stat.SF_APPEND: 文件只能追加内容(超级用户可设)
        stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
        stat.SF_SNAPSHOT: 快照文件(超级用户可设)
"""

path = "D:\\window\\temp\\test.txt"

# 为文件设置标记，使得它不能被重命名和删除
flags = stat.SF_NOUNLINK
os.chflags(path, flags)
