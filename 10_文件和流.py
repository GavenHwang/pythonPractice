
# 文件模式：
# 'r'   读模式
# 'w'   写模式
# 'a'   追加模式
# 'b'   二进制模式（可以添加到其他模式中使用）
# '+'   读/写模式（可以添加到其他模式中使用）
# Windows下使用文本模式读写文件时会自动将\r\n转为\n,将\n转换为\r\n
# 打开二进制文件时一定要使用‘二进制’模式，避免自动转换
# 缓冲参数：0或者False表示不使用缓冲，1或者True表示使用缓冲，使用缓冲时只有在flush和close时才会写入磁盘
# 负数表示使用默认缓冲区大小，正数表示缓冲区大小，单位是字节

# somescript.py
# cat a.txt | python somescript.py
# import sys
#
# text = sys.stdin.read()   # stdin表示从表中流中读取
# words = text.split()
# print(len(words))

# offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
# whence：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。
# f = open(r'D:\1.txt', 'wb+')    # 注意：使用二进制模式
# f.write(b'123456789')           # 注意：写入的是二进制格式
# f.seek(2)
# print(f.read(1))
# f.seek(2, 1)
# print(f.read(1))

# f = open(r'D:\1.txt')
# print(f.read(3))    # 默认从开始读三个字节
# print(f.read(5))    # 从上次读到的地方读5个字节
# print(f.tell())     # 打印读到的位置
# f.close()

# readline、readlines、read
# writelines、write  没有writeline方法，writelines不会自动新增行

# with open(r'D:\1.txt') as f:
#     print(f.read(4))

# f = open(r'hello.py', 'br')
# print(f.read(4))
# print(f.read(7))
# f.close()

# f = open(r'hello.py', 'br')
# print(f.read())
# f.close()
#
# f = open(r'hello.py', 'br')
# for i in range(10):
#     print(i, f.readline())

# f = open(r'hello.py', 'br')
# print(f.readlines())

# f = open(r'hello.py', 'bw')
# f.write(b'0123456789')
# f.close()

# f = open(r'database.py', 'br')
# lines = f.readlines()
# print(lines)
# f.close()
# w = open(r'hello.py', 'bw+')
# w.writelines(lines)
# w.close()

# 对文件内容进行迭代
# 这个字节迭代
# f = open(r'hello.py', 'r', encoding='UTF-8')
# char = f.read(1)
# while char:
#     # process(char)
#     char = f.read(1)
#     print(char, end='')
# f.close()

# 优化while循环
# f = open(r'hello.py', 'r', encoding='UTF-8')
# while True:
#     char = f.read(1)
#     print(char, end='')
#     if not char:
#         break
# f.close()

# 逐行迭代
# f = open(r'hello.py', 'r', encoding='UTF-8')
# while True:
#     line = f.readline()
#     print(line, end='')
#     if not line:
#         break
# f.close()

# 一次读取整个文件
# f = open(r'hello.py', 'r', encoding='UTF-8')
# for v in f.read():
#     print(v, end='')
# f.close()

# 惰性迭代
# import fileinput
#
# from pip._vendor import chardet
#
# for line in fileinput.input(r'hello.py', mode='rb'):
#     # 获得编码格式
#     encoding = chardet.detect(line).get('encoding')
#     print(line.decode(encoding), end='')

# 文件迭代器
# f = open(r'hello.py', 'r', encoding='UTF-8')
# for line in f:
#     print(line, end='')
# f.close()

# for line in open(r'hello.py', 'r', encoding='UTF-8'):
#     print(line, end='')

import sys

# 标准输入也是可以迭代的
# for line in sys.stdin:
#     print(line)

f = open(r'test.txt', 'w')
f.write("hello\n")
f.write("world\n")
f.write("python\n")
f.close()
lines = list(open('test.txt'))
print("lines:", lines)
one, two, three = open('test.txt')
print(one, two, three, sep='')
