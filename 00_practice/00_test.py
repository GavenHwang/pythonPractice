# -*- coding: utf-8 -*-
# import struct
#
# # 定义编码格式
# fmt = ">I4s6s"
# # 构造数据
# method = b"GET"
# path = b"/index.html"
# body = b"88.111.19/001"
# data = (len(method) + len(path) + len(body), method, path, body)
# # 编码数据
# packed_data = struct.pack(fmt, *data)
# # 解妈数据
# unpacked_data = struct.unpack(fmt, packed_data)
# print("Encoded data: ", packed_data)
# print("Decoded data: ", unpacked_data)
import sys
