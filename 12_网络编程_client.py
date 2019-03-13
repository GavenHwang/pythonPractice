# -*- coding: utf-8 -*-

# **************** socket client ************
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
s.send(b"hello server! I'm client.")
print(s.recv(1024))
