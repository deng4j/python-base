import socket

udp_socket = None


def initUDP():
    global udp_socket

    # 创建socket
    # AF_INET 表示ip地址，也是internet互联⽹
    # SOCK_DGRAM 表示使⽤udp 协议
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def sender(send_content, address):
    send_data = send_content.encode("utf-8")

    # ("192.168.31.221", 8080) 接收数据⽅ip地址和端⼝
    udp_socket.sendto(send_data, address)


if __name__ == '__main__':
    print("-------------- 欢迎进入UDP系统-------------------")

    addr = ("127.0.0.1", 8080)
    initUDP()  # 初始化

    while True:
        content = input("请输入消息：")
        if content == "exit":
            # 关闭数据
            udp_socket.close()

        sender(content, addr)
