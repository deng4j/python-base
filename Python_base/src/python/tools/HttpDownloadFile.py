def urllib_download(IMAGE_URL, folderPath, suffix):
    from urllib.request import urlretrieve
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    import time
    folderPath = folderPath + '/' + str(time.time()) + suffix
    urlretrieve(IMAGE_URL, folderPath)
    return folderPath


def downloadRsc(url, folderPath, suffix):
    import urllib.request
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    import time
    folderPath = folderPath + '/' + str(time.time()) + suffix
    rsc = urllib.request.urlopen(url)
    with open(folderPath, 'wb') as f:
        f.write(rsc.read())


def request_download(IMAGE_URL, folderPath, suffix):
    import requests
    import time
    folderPath = folderPath + '/' + str(time.time()) + suffix
    r = requests.get(IMAGE_URL)
    with open(folderPath, 'wb') as f:
        f.write(r.content)


def chunk_download(IMAGE_URL, folderPath, suffix):
    import requests
    import time
    r = requests.get(IMAGE_URL, stream=True)
    folderPath = folderPath + '/' + str(time.time()) + suffix
    with open(folderPath, 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)


"""
从网上下载文件到本地
"""
if __name__ == '__main__':
    path = input("输入path：")
    print(path)
    while True:
        url = input("输入url：")
        urllib_download(url, path, '.png')
