import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(('127.0.0.1', 8080))  # 为客户端绑定一个固定的地址，ip和端口

while True:
    print('---------------初始化完成------------------')
    result = client.recvfrom(1024)
    print(result)
