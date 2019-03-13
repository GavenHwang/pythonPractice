# -*- coding: utf-8 -*-

# ****************** socket server ****************
# import socket
#
# s = socket.socket()
#
# host = socket.gethostname()
# port = 1234
# s.bind((host, port))
#
# s.listen(5)
# while True:
#     c, addr = s.accept()
#     print("Got connection from ", addr)
#     c.send(b'Thank you for connecting')
#     c.close()

# ****************** urllib *******************
# from urllib.parse import quote, quote_plus
# from urllib.request import urlopen
#
# webpage = urlopen('http://www.baidu.com')
# localfile = urlopen(r'file: D:\1.txt')
#
# print(localfile.read())
# print(webpage.read())

# 获取远程文件
# from urllib.request import urlretrieve
#
# urlretrieve("http://www.baidu.com", "baidu.html")
# 将URL中的特殊字符替换为对URL友好的字符,默认是 /
# print(quote("http://www.baidu.com?db=test", safe=':/')) # 不对:和/
# print(quote_plus("http://www.baidu.com?db=ha ha"))  # 使用+号代替空格

# ************************** SocketServer之TCPServer示例 ******************
# UDPServer, UnixStremServer和UnixDatagramServer很少使用到
# from socketserver import StreamRequestHandler, TCPServer
#
#
# class Handler(StreamRequestHandler):
#     def handle(self):
#         host, port = self.request.getpeername()
#         print('Got connection from', host+':'+str(port))
#         self.wfile.write(b'Thank you for connecting')
#
#
# server = TCPServer(('', 1234), Handler)     # '' 表示主机名
# server.serve_forever()

# 分叉: Unix术语(Windows不支持);将一个进程复制为两个,有主次之分,可以分别去执行不同的任务;无同步问题;耗费资源
# 线程: 轻量级的进程或者子进程,所有线程存在于相同的进程中,共享内存;资源耗费低;有同步问题
# 微线程: 类线程的并行形式,伸缩性好

# *************** 使用分叉技术的服务器示例(不支持windows) **************
# from socketserver import ForkingMixIn, TCPServer, StreamRequestHandler
#
#
# class Server(ForkingMixIn, TCPServer):
#     pass
#
#
# class Handler(StreamRequestHandler):
#     def handle(self):
#         addr = self.request.getpeername()
#         print('Got connection from ', addr)
#         self.wfile.write('Thank you for connecting')
#
#
# server = Server(('', 1234), Handler)
# server.serve_forever()

# *************** 使用线程技术的服务器示例 **************
# from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler
#
#
# class Server(ThreadingMixIn, TCPServer):
#     pass
#
#
# class Handler(StreamRequestHandler):
#     def handle(self):
#         addr = self.request.getpeername()
#         print("Got connection from ", addr)
#         self.wfile.write(b'Thank you for connecting')
#
#
# server = Server(('', 1234), Handler)
# server.serve_forever()

# ************* select简单服务器 *************
# import select
# import socket
#
# s= socket.socket()
#
# host = socket.gethostname()
# port = 1234
# s.bind((host, port))
#
# s.listen(5)
# inputs = [s]
# while True:
#     rs, ws, es = select.select(inputs, [], [], 3)
#     for r in rs:
#         if r is s:
#             c, addr = s.accept()
#             print('Got connection from ', addr)
#             # c.send(b'Thank you for connecting')
#             inputs.append(c)
#         else:
#             try:
#                 print("try")
#                 data = r.recv(1024)
#                 disconnected = not data
#             except socket.error:
#                 print('except')
#                 disconnected = True
#
#             if disconnected:
#                 print(r.getpeername(), 'disconnected')
#                 inputs.remove(r)
#             else:
#                 print(data)

# *************** poll简单服务器 *******************
# import socket, select
#
# s = socket.socket()
# host = socket.gethostname()
# port = 1234
# s.bind((host, port))
# fdmap = {s.fileno(): s}
# s.listen(5)
# p = select.poll()
# p.register(s)
# while True:
#     events = p.poll()
#     for fd, event in events:
#         if fd == s.fileno():
#             c, addr = s.accept()
#             print('Got connection from ', addr)
#             p.register(c)
#             fdmap[c.fileno()] = c
#         elif event & select.POLLIN:     # POLLIN 读取来自文件描述符的数据
#             data = fdmap[fd].recv(1024)
#             if not data:
#                 print(fdmap[fd].getpeername(), 'disconnected')
#                 p.unregister(fd)
#                 del fdmap[fd]
#             else:
#                 print(data)

# **************** 使用twisted的简单服务器 ********************
# from twisted.internet import reactor
# from twisted.internet.protocol import Protocol, Factory
#
#
# class SimpleLogger(Protocol):
#     def connectionMade(self):
#         print("Got connection from", self.transport.client)
#
#     def connectionLost(self, reason):
#         print(self.transport.client, 'disconnected')
#
#     def dataReceived(self, data):
#         print(data)
#
#
# factory = Factory()
# factory.protocol = SimpleLogger
#
# reactor.listenTCP(1234, factory)
# reactor.run()

# 使用LineReceiver协议改进
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.protocols.basic import LineReceiver


class SimpleLogger(LineReceiver):
    def connectionMade(self):
        print("Got connection from", self.transport.client)

    def connectionLost(self, reason):
        print(self.transport.client, 'disconnected')

    def dataReceived(self, data):
        print(data)

    def lineReceived(self, line):
        print(line)


factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1234, factory)
reactor.run()