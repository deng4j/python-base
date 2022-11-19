import urllib.request
import urllib.error

"""
urllib.error 模块为 urllib.request 所引发的异常定义了异常类，基础异常类是 URLError。

urllib.error 包含URLError 和 HTTPError。
"""

print("------------------------------------error------------------------------------------")

try:
    myURL2 = urllib.request.urlopen("https://www.runoob.com/no.html")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print('---404---')
