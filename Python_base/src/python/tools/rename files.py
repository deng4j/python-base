import os


def rename_files(path, suffix, st):
    """
    批量删除文件名的某个字符串
    :return:
    """
    os.chdir(path)  # 更改工作路径
    filelist = os.listdir(path)
    print(filelist)  # 文件夹中所有文件名
    for file_name in filelist:
        if file_name.endswith(suffix):
            new_name = file_name.replace(st, '')
            os.rename(file_name, new_name)  # 重命名

    print("修改完毕")


if __name__ == '__main__':
    path = '/Users/deng4j/development/doc/doc/计算机/操作系统/unix/linux/实例/WMware装载Centos7/images'
    suffix = '.png'
    st = 'QQ截图'
    rename_files(path, suffix, st)
