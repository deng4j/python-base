import os


def deleteByFind(folderPath, strs):
    """用于在某个文件夹下批量删除包含某个字符串的文件"""
    if folderPath is None or folderPath == '':
        raise Exception('path为空')

    if not folderPath.endswith('/'):
        folderPath = folderPath + '/'

    for fname in os.listdir(folderPath):
        if fname.find(strs) != -1:
            print("删除文件：", fname)
            os.remove(folderPath + fname)


if __name__ == '__main__':
    path = '/Users/deng4j/development/pycharm_project/project3_web_crawler/CrawlerModule/a_doc/day4/images'
    deleteByFind(path, '(1)')
