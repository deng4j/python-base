import urllib.request

"""
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)：
    url：url 地址。
    data：发送到服务器的其他数据对象，默认为 None。
    timeout：设置访问超时时间。
    cafile 和 capath：cafile 为 CA 证书， capath 为 CA 证书的路径，使用 HTTPS 需要用到。
    cadefault：已经被弃用。
    context：ssl.SSLContext类型，用来指定 SSL 设置。
    
read(len) 是读取缓冲区的网页内容,可以指定读取的长度
readline() - 读取缓冲区的一行内容
readlines() - 读取缓冲区的全部内容，它会把读取的内容赋值给一个列表变量。
getcode() 函数获取网页状态码
"""

print("----------------------------- read ------------------------------------")

myURL = urllib.request.urlopen("https://www.Baidu.com/")
print(myURL.getcode())
print(myURL.read(10))
print(myURL.read())

print("----------------------------- readline ------------------------------------")

myURL = urllib.request.urlopen("https://www.Baidu.com/")
print(myURL.readline())

lines = myURL.readlines()
for line in lines:
    print(line)

