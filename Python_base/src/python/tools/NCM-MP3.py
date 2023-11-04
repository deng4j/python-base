from ncmdump import dump
import os, fnmatch

print("如留空，默认: C:\\CloudMusic\\")
download_folder = input("下载路径：") or "C:\\CloudMusic\\"
os.system('cls')
waiting = True
print("当前下载路径：" + download_folder)
print("等待转换...")


def all_files(root, patterns='*', single_level=False, yield_folder=False):
    patterns = patterns.split(';')
    for path, subdirs, files in os.walk(root):
        if yield_folder:
            files.extend(subdirs)
        files.sort()
        for fname in files:
            for pt in patterns:
                if fnmatch.fnmatch(fname, pt):
                    yield os.path.join(path, fname)
                    break
        if single_level:
            break


while 1:
    thefile = list(all_files(download_folder, '*.ncm'))
    for item in thefile:
        if (waiting == True):
            waiting = False
            os.system('cls')
        print(dump(item), "转换成功！")
        delete = os.remove(item)
