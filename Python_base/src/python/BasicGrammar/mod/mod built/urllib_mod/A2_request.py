import urllib.request

"""
URL 的编码与解码可以使用 urllib.request.quote() 与 urllib.request.unquote()

urllib.request.Request(url, data=None, headers={}, 
    origin_req_host=None, unverifiable=False, method=None)：对 headers（网页头信息）进行模拟。
        url：url 地址。
        data：发送到服务器的其他数据对象，默认为 None。
        headers：HTTP 请求的头部信息，字典格式。
        origin_req_host：请求的主机地址，IP 或域名。
        unverifiable：很少用整个参数，用于设置网页是否需要验证，默认是False。。
        method：请求方法， 如 GET、POST、DELETE、PUT等。
"""

print("----------------------------------- quote ---------------------------------------")

encode_url = urllib.request.quote("https://www.Baidu.com/")
print(encode_url)

unencode_url = urllib.request.unquote(encode_url)
print(unencode_url)

print("----------------------------------- Request ---------------------------------------")

url = 'https://www.Baidu.com/s?wd='
keyword = 'Python 教程'
key_code = urllib.request.quote(keyword)  # 对请求进行编码
url_all = url + key_code

header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666 Edg/105.0.0.0'
}

request = urllib.request.Request(url_all, headers=header)
reponse = urllib.request.urlopen(request).read()

fh = open("D:\\window\\temp\\search.html", "wb")  # 将文件写入到当前目录中
fh.write(reponse)
fh.close()
