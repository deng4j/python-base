import io

"""
BytesIO实现了在内存中读写bytes
"""

from src.python.tools.GetRootFolder import getRepositoryRootPath

root_paths = getRepositoryRootPath()

img_url = root_paths + 'Python_base/src/resources/imgs/斋藤飞鸟.jpg'

with open(img_url, 'rb') as f:
    a = f.read()

# 将字节对象转为Byte字节流数据,供Image.open使用
byte_stream = io.BytesIO(a)

img_url1 = root_paths + 'Python_base/src/resources/imgs/斋藤飞鸟(1).jpg'

f = open(img_url1, 'wb')
f.write(byte_stream.read())
