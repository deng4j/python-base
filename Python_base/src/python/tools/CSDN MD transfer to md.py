import re

from tools.HttpDownloadFile import urllib_download

"""
CSDN MD（网络图片）转化下载到本地.md
"""

http_local = {}

path_md = ''
path_assist = ''


def regex_http(line):
    return re.finditer(r'(https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?',
                       line)


def get_http_png():
    file = open(path_md, 'r')
    lines = file.readlines()
    for line in lines:
        results = regex_http(line)
        for result in results:
            if result.group().find('img-blog') != -1:
                http_local[result.group()] = ''
    return lines


def download_png():
    for key in http_local.keys():
        filename = urllib_download(key, path_assist, '.png')
        http_local[key] = filename


def write_md(file_md, path_new_md):
    out = open(path_new_md, "w+")
    for line in file_md:
        results = regex_http(line)
        for result in results:
            if result.group().find('img-blog') != -1:
                line = line.replace(result.group(), http_local[result.group()])
        out.write(line)
    out.close()


"""
不能有中文路径
"""
if __name__ == '__main__':
    path_md = '/Users/deng4j/development/idea_project/project2/JavaServer/SpringCloud/a_doc/Otter/Otter.md'
    path_assist = '/Users/deng4j/development/idea_project/project2/JavaServer/SpringCloud/a_doc/Otter/assist'
    path_new_md = '/Users/deng4j/development/idea_project/project2/JavaServer/SpringCloud/a_doc/Otter/new.md'
    file_md = get_http_png()
    print(http_local)
    download_png()
    write_md(file_md, path_new_md)
