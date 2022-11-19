"""
Python 提供了两个级别访问的网络服务。：
    1.低级别的网络服务支持基本的 Socket，它提供了标准的 BSD Sockets API，可以访问底层操作系统Socket接口的全部方法。
    2.高级别的网络服务模块 SocketServer， 它提供了服务器中心类，可以简化网络服务器的开发。

socket.socket([family[, type[, proto]]])：
    family: 套接字家族
        PF_INET, AF_INET： Ipv4⽹络协议
        PF_INET6, AF_INET6： Ipv6⽹络协议
        AF = Address Family
        PF = Protocol Family
    type: 套接字类型
        SOCK_STREAM： 提供⾯向连接的稳定数据传输，即TCP协议。
        OOB： 在所有数据传送前必须使⽤connect()来建⽴连接状态。
        SOCK_DGRAM： 使⽤不连续不可靠的数据包连接，即UDP。
        SOCK_SEQPACKET： 提供连续可靠的数据包连接。
        SOCK_RAW： 提供原始⽹络协议存取。
        SOCK_RDM： 提供可靠的数据包连接。
        SOCK_PACKET： 与⽹络驱动程序直接通信。
    protocol: 一般不填默认为0.

socket.setsockopt(level, optname, value)在套接字级别上(SOL_SOCKET)，option_name可以有以下取值：
    SO_DEBUG，打开或关闭调试信息。
    SO_REUSEADDR，打开或关闭地址复⽤功能。
    SO_DONTROUTE，打开或关闭路由查找功能。
    SO_BROADCAST，允许或禁⽌发送⼴播数据。
    SO_SNDBUF，设置发送缓冲区的⼤⼩。其上限为256 * (sizeof(struct sk_buff) + 256)，下限为 2048字节。
    SO_RCVBUF，设置接收缓冲区的⼤⼩。上下限分别是：256 * (sizeof(struct sk_buff) + 256)和 256字节。
    SO_KEEPALIVE，套接字保活。
    SO_OOBINLINE，紧急数据放⼊普通数据流。
    SO_NO_CHECK，打开或关闭校验和。
    SO_PRIORITY，设置在套接字发送的所有包的协议定义优先权。
    SO_LINGER，如果选择此选项, close或 shutdown将等到所有套接字⾥排队的消息成功发送或到 达延迟时间后才会返回. 否则, 调⽤将⽴即返回。
    SO_PASSCRED，允许或禁⽌SCM_CREDENTIALS 控制消息的接收。
    SO_TIMESTAMP，打开或关闭数据报中的时间戳接收。
    SO_RCVLOWAT，设置接收数据前的缓冲区内的最⼩字节数。
    SO_RCVTIMEO，设置接收超时时间。
    SO_SNDTIMEO，设置发送超时时间。
    SO_BINDTODEVICE，将套接字绑定到⼀个特定的设备上。
    SO_ATTACH_FILTER和SO_DETACH_FILTER。

Socket对象：
    服务器端套接字
    s.bind()	绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址。
    s.listen()	开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
    s.accept()	被动接受TCP客户端连接,(阻塞式)等待连接的到来

    客户端套接字
    s.connect()	主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。
    s.connect_ex()	connect()函数的扩展版本,出错时返回出错码,而不是抛出异常

    公共用途的套接字函数
    s.recv()	接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。
    s.send()	发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。
    s.sendall()	完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
    s.recvfrom()	接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
    s.sendto()	发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。
    s.close()	关闭套接字
    s.getpeername()	返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
    s.getsockname()	返回套接字自己的地址。通常是一个元组(ipaddr,port)
    s.setsockopt(level,optname,value)	设置给定套接字选项的值。
    s.getsockopt(level,optname[.buflen])	返回套接字选项的值。
    s.settimeout(timeout)	设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()）
    s.gettimeout()	返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。
    s.fileno()	返回套接字的文件描述符。
    s.setblocking(flag)	如果 flag 为 False，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用 recv() 没有发现任何数据，或 send() 调用无法立即发送数据，那么将引起 socket.error 异常。
    s.makefile()	创建一个与该套接字相关连的文件
"""

"""
TCP可靠，UDP不可靠的原因--SO_RCVBUF 、SO_SNDBUF：
    每个TCP socket在内核中都有⼀个发送缓冲区和⼀个接收缓冲区，TCP的全双⼯的⼯作模式以及 TCP的滑动窗⼝便是依赖于这两个独⽴的buffer
    以及此buffer的填充状态。接收缓冲区把数据缓存⼊内核，应⽤进程⼀直没有调⽤read进⾏读取的话， 此数据会⼀直缓存在相应socket的接收缓冲区内。
    再啰嗦⼀点，不管进程是否读取socket，对端发来的数据都会经由内核接收并且缓存到socket的 内核接收缓冲区之中。read所做的⼯作，
    就是把内核缓冲区中的数据拷⻉到应⽤层⽤户的buffer ⾥⾯，仅此⽽已。 进程调⽤send发送的数据的时候，将数据拷⻉进⼊socket的内核发送缓冲区之中，
    然后send便会 在上层返回。换句话说，send返回之时，数据不⼀定 会发送到对端去，send仅仅是把应⽤层buffer的数据拷⻉进socket的内核发送buffer中。
    每个UDP socket都有⼀个接收缓冲区，没有发送缓冲区，从概念上来说就是只要有数据就发，不 管对⽅是否可以正确接收 对于TCP，如果应⽤进程⼀直没有读取，
    buffer满了之后，发⽣的动作是：通知对端TCP协议中 的窗⼝关闭。这个便是滑动窗⼝的实现。保证TCP套接⼝ 接收缓冲区不会溢出，从⽽保证了TCP是可靠传输。
    因为对⽅不允许发出超过所通告窗⼝⼤⼩的 数据。 这就是TCP的流量控制，如果对⽅⽆视窗⼝⼤⼩ ⽽发出了超过窗⼝⼤⼩的数据，则接收⽅TCP将丢弃它。 
    对于UDP，当套接⼝接收缓冲区满 时，新来的数据报⽆法进⼊接收缓冲区，此数据报就被丢弃。
"""