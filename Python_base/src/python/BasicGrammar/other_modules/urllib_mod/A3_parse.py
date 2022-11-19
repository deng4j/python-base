import urllib.request
import urllib.parse

"""
urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)：用于解析 URL
    urlstring 为 字符串的 url 地址
    scheme 为协议类型
    allow_fragments 参数为 false，则无法识别片段标识符。相反，它们被解析为路径，参数或查询组件的一部分，并 fragment 在返回值中设置为空字符串。
"""

print("------------------------------------urlparse------------------------------------------")

o = urllib.parse.urlparse("https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B")
print(o)

print("-------------------------------------urlencode-----------------------------------------")

url = 'https://www.runoob.com/try/py3/py3_urllib_test.php'  # 提交到表单页面
data = {'name': 'RUNOOB', 'tag': '菜鸟教程'}  # 提交数据
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666 Edg/105.0.0.0'
}

data = urllib.parse.urlencode(data).encode('utf8')  # 对参数进行编码，解码使用 urllib.parse.urldecode

request = urllib.request.Request(url, data, header)  # 请求处理
reponse = urllib.request.urlopen(request).read()  # 读取结果

fh = open("D:\\window\\temp\\form.html", "wb")
fh.write(reponse)
fh.close()
