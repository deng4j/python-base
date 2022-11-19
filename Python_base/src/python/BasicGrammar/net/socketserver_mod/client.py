import socket

tcp_clinet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_clinet.connect(('127.0.0.1',8080))
while True:
    send_data = input('输入：\n')
    tcp_clinet.sendall(send_data.encode())
    if send_data == 'close':
        print('closed!!!')
        break
    info = tcp_clinet.recv(1024).decode()
    print(info)