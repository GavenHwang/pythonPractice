# -*- coding:utf-8 -*-
import socket

# 创建 socket
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定 IP 和端口号
sk.bind(('127.0.0.1', 6000))
while True:
    # 接收数据报
    msg, addr = sk.recvfrom(1024)
    # 打印(python2.7 不需要decode)
    print('来自[%s:%s]的消息: %s' % (addr[0], addr[1], msg.decode('utf-8')))

    if msg.decode('utf-8') == "hello":
        reply = 'hi'
    else:
        reply = 'what did you say'

    # 发送数据报
    sk.sendto(reply.encode('utf-8'), addr)

# 关闭 socket
# sk.close()
