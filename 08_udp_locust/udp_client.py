# -*- coding:utf-8 -*-
import socket

# 创建 socket
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('127.0.0.1', 6000)
while True:
    # 等待输入，python2.7输入'hello'时需要带引号
    msg = input('>>>')
    # 发送数据报
    sk.sendto(msg.encode('utf-8'), addr)
    # 接收数据报
    msg_recv, addr = sk.recvfrom(1024)
    # 打印
    print(msg_recv.decode('utf-8'))

# 关闭 socket
# sk.close()