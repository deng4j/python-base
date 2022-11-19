import requests

"""
有些请求不成功，可能需要Referer或Cookie
"""

url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=失信人&pn=0&rn=10&ie=utf-8&oe=utf-8'

headers = {
    # 伪装成了Mac火狐浏览器
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0",
}

resp = requests.get(url, headers=headers)

print(resp.content.decode())
