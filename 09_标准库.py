# -*- coding: utf-8 -*-

# ********************* SYS ***************************
import sys
# sys.argv 表示外部调用当前脚本时的参数
# eg. D:\test.py a b c
# sys.argv的值为['D:\\test.py', 'a', 'b', 'c'],第一个参数为当前脚本，之后是参
# print(sys.argv)

# sys.exit()用于退出当前程序参数为code，一般用于sys.exit(0)或者sys.exit(1),finally中的字句会照常执行
# for i in range(5):
#     try:
#         if i == 3:
#             sys.exit(1)
#         else:
#             print(i)
#     except Exception:
#         pass
#     finally:
#         print("the end")

# sys.modules是一个全局字典，该字典是python启动后就加载在内存中。
# 每当程序员导入新的模块，sys.modules都将记录这些模块。字典sys.modules对于加载模块起到了缓冲的作用。
# 当某个模块第一次导入，字典sys.modules将自动记录该模块。当
# 第二次再导入该模块时，python会直接到字典中查找，从而加快了程序运行的速度。
# 字典sys.modules具有字典所拥有的一切方法，可以通过这些方法了解当前的环境加载了哪些模块
# print(sys.modules.keys())
# print(sys.modules.values())

# sys.path 输出系统模块路径
# import pprint
# pprint.pprint(sys.path)
# print(sys.path)

# sys.platform输出python解释器正在其上运行的“平台”
# print(sys.platform)

import os

# ********************************* OS ***********************************
# 一些os模块变量
# os.environ表示系统环境变量的字典，比如 os.environ['PYTHONPATH']
# print(os.environ)

# os.system(command) 提供类似于cmd命令的功能
# os.system("cd C:\\Users")

# 输出系统路径分割符，windows下是“\”, linux下是“/”, Mac OS下是“::”
# print(os.sep)

# 输出系统换行符，windows下是“\r\n”, linux下是“\n”, Mac OS下是“\r”
# print(os.linesep)

# 返回字节的加密强随机数
# print(os.urandom(2))

# 打开火狐浏览器, startfile允许带空格的路径
# os.system(r'D:\"Program Files"\"Mozilla Firefox"\firefox.exe')
# os.startfile(r'D:\Program Files\Mozilla Firefox\firefox.exe')
# 打开百度首页
# import webbrowser
#
# webbrowser.open('http://www.baidu.com')

# *************************** FILEINPUT **************************
# test.py test.txt
# import fileinput
#
# for line in fileinput.input(inplace=False):
#     line = line.rstrip()
#     num = fileinput.lineno()    # 当前行数，如果遍历两个文件，会累加
#     print("%-80s # %03i" % (line, num))
# fileinput.close()

# 返回遍历对象, inplace=True会将打印内容覆盖原内容
# backup会备份源文件，备份文件名为源文件名+backup
# fileinput.input(inplace=True, backup='2.txt')
# fileinput.filename()        # 文件名
# fileinput.lineno()          # 当前行数
# fileinput.filelineno()      # 当前文件的行数
# fileinput.isfirstline()     # 是否是第一行
# fileinput.isstdin()         # 最后一行是否来自sys.stdin
# fileinput.nextfile()        # 关闭当前文件，移动到下一个文件 if fileinput.isstdin(): fileinput.nextfile()
# fileinput.close()           # 关闭序列


# ******************** 集合、堆和双端队列 ***********************
# 集合主要用于检查成员资格，因此副本是被忽略的, 另外，与字典一样集合也是无序的
# print(set([1, 1, 2, 2, 3, 3]))      # {1, 2, 3}
# a = set(iter([1, 2, 3]))
# b = set(iter([2, 3, 4]))
# c = a & b
# # 集合操作
# print(a.union(b))
# print(a | b)
#
# print(a & b)
# print(a.intersection(b))
#
# print(c.issubset(a))
# print(c < a)
#
# print(a.issuperset(c))
# print(a >= c)
#
# print(a.difference(b))
# print(a - b)
#
# print(a.symmetric_difference(b))
# print(a ^ b)
#
# print(a.copy())
# print(a.copy() is a)
# from functools import reduce
#
# myset = []
# for i in range(10):
#     myset.append(set(range(i, i + 5)))
# print(reduce(set.union, myset))
# help(set)

# 集合是可变的所以不能用来做字典中的键，而且集合只能包含不可变的元素，所以集合不能包含集合
# 但是frozenset是不可变的，所以集合中可以包含frozenset
# a = set(iter([1, 2, 3]))
# b = set(iter([2, 3, 4]))
# a.add(frozenset(b))
# print(a)

# ***************** 堆 *********************
# from heapq import *
# from random import shuffle
#
# data = list(range(5))
# shuffle(data)
# heap = []
# for n in data:
#     heappush(heap, n)
# print(heap)
#
# # 堆属性：2i以及2i+1位置的元素总比i/2位置的元素大
# for i in range(len(heap) - 1):
#     if 2*i + 3 <= len(heap):
#         print(heap[i], heap[2*i+1], heap[2*i+2], heap[2*i+1] > heap[i] < heap[2*i+2])

# heappush()          # 入堆
# heappush(heap, 3)
# print(heap)
# heappop()           # 弹出最小元素，一般来说都是 索引为0处的元素，弹出元素之后会确保把最小的元素放在索引0处
# print(heappop(heap))
# heapify()           # 使用任意列表作为参数，将其转换为合法的堆
# a = [1, 3, 4, 2, 5]
# print(heapify(a))
# print(a)
# heapreplace()       # 弹出最小元素，并将新元素推入堆中，比 先pop在push高效
# heapreplace(a, 6)
# print(a)
# nlargest(n, heap)   # 返回堆中前n大的数
# print(nlargest(3, a))
# nsmallest(n, heap)  # 返回堆中前n小的数
# print(nsmallest(2, a))

# ********************* 双端队列 ****************************
# from collections import deque
#
# q = deque(range(5))
# q.append(5)
# q.append(6)
# q.appendleft(7)
# print(q)
# print(q.pop())
# print(q.popleft())
# q.rotate(3)         # 将列表后n项移动到左侧[0, 1, 2, 3, 4, 5] --> [5, 4, 3, 0, 1, 2]
# print(q)

# ****************************** time ********************************
# import time

# time.asctime()    将时间元组转换为字符串, 默认为当前时间    Fri Feb 22 17:40:51 2019
# print('time.asctime(): ' + time.asctime(time.localtime(3600)) + '')
# print(time.asctime(time.localtime()))
# time.localtime()  将秒数转化为日期元组，以本地时间为准  time.struct_time(tm_year=2019, tm_mon=2, tm_mday=22, tm_hour=17, tm_min=40, tm_sec=22, tm_wday=4, tm_yday=53, tm_isdst=0)
# print(time.localtime(time.time()))
# time.mktime()     将时间元组转换为本地时间(秒)
# print(time.mktime(time.localtime()))
# time.sleep()      休眠
# time.strftime()   将时间元组解析为字符串
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '')

# 将时间字符串转为日期元组
# time_str = '1970-01-01 09:00:00'
# time_tuple = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
# 将时间字符串转为本地时间（秒）
# print(time.mktime(time.strptime('1970-01-01 09:00:00', "%Y-%m-%d %H:%M:%S")))

# a = "Sat Mar 28 22:24:24 2016"
# print(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
# print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
# time.time()       当前时间

# ******************************* random ***************************************
from random import *
# from time import *

# print(random())                  # 返回0到1之间的伪随机数

# print(getrandbits(3))            # 以长整型的形式返回n个随机位
# 8 bit = 1 Byte，不管它们都是全是0、全是1或者是由若干0和若干1混合而成。
# eg: getrandbits(2),表示返回两位bit数，即 00 ~ 11，即，0,1,2,3
# getrandbits(3),表示返回两位bit数，即 00 ~ 111，即，0,1,2,3,4,5,6,7
# 原理如下：
# import random
# from os import urandom
# from math import ceil
# k = 2
# a = ceil(k/8)
# b = int.from_bytes(urandom(a), 'big')
# c = b >> (a*8 - k)
# print(c)

# print(uniform(1, 5))             # 返回随机数n，其中1<=n<5
# print(randrange(1, 20, 2))       # 返回小于20的正奇数
# print(choice([1,2,3,4,5,6,'a','b','c','d']))    # 从给定序列中选择随机元素
# a = [1,2,3,4,5]
# shuffle(a)
# print(a)                                # 将给定的序列随机排序，每种排列可能性都是近似相等的
# print(sample([1,2,3,4,5], 2))    # 从给定序列中随机选择出n个

# random示例1. 随机打印2008-2018年之间的日期（-1表示一周中的某一天，一年中的某一天，一年中的某天和夏令时）
# date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
# date2 = (2018, 1, 1, 0, 0, 0, -1, -1, -1)
# time1 = mktime(date1)
# time2 = mktime(date2)
# print(strftime("%Y-%m-%d %H:%M:%S", localtime(uniform(time1, time2))))

# 掷筛子
# num = int(input("How many dice?"))
# sides = int(input("How many sides per die?"))
# sum = 0
# for i in range(num):
#     sum += randrange(sides) + 1
# print("the result is ", sum)

# 从输入的文件中随机选择一行内容
# import random, fileinput
#
# fortunes = list(fileinput.input())
# print(random.choice(fortunes))

# 洗牌
# from random import *
#
# values = list(range(1, 11)) + 'Jack Queen King'.split()
# suits = "spades hearts clubs diamonds".split()
# deck = ['%s of %s' % (v, s) for v in values for s in suits]
# deck.extend(['tetrarch', 'king'])
# shuffle(deck)
# while deck:
#     ignore = input(deck.pop())

# *************************** shelve ********************************
# import shelve

# writeback为true时，会将改动放在缓存，在close时才真正写入到磁盘
# s = shelve.open(r'D:\Users\Gaven\PycharmProjects\pythonPractice\a.txt', writeback=True)
# s['x'] = [1, 2, 3]
# # s['x'].append(4)
# temp = s['x']
# temp.append(4)
# s['x'] = temp
# print(s['x'])
# s.close()

# import database
#
# database.main()


# ******************************** re ********************************
import re

# 通配符、转义、字符集
# . 号只能匹配一个任意字符（不包括换行符），'.'号转义需要'\\.'
# [a-zA-Z0-9] 表示任意一个字母或者数字，[^abc]表示除了‘abc’之外的任意一个字符
# 为了避免使用转义符号，^不应该出现在首字母，]和- 应该放在字符集的开头，否则必须用\进行转义
# str = 'abc python.org def'
# r = 'python\\.org'      # \\表示一个\, \. 表示 .
# r = r'python\.org'      # 与上面效果相同
# print(re.findall(r, str))

# 选择符和子模式
# str = 'python&perl'
# r = '(ython|perl)'
# print(re.findall(r, str))

# 可选项和重复子模式
# r = r'(http://)?(www\.)?python\.org'
# (pattern)?        :允许出现一次或者根本不出现
# (pattern)*        :允许出现0次或者多次
# (pattern)+        :允许出现一次或者多次
# (pattern){m,n}    :允许出现m~n次或者根本不出现

# 字符串的开始和结尾
# ^ 表示字符串开始 $ 表示字符串结尾
# str1 = 'http://www.baidu.com'
# str2 = 'www.http://baidu.com'
# r = r'^http.*'
# print(re.findall(r, str1))
# print(re.findall(r, str2))

# str = 'aaapython&pearlbbb'
# r = r'p(ython|earl)'
# p = re.compile(r)
# print(p.findall(str))
# print(re.match(r, str))
# compile   :將正则表达式转为模式对象
# search    :寻找第一个匹配到的子字符串
# match     :从字符串开头匹配，如果子字符串不在开头则返回None
# some_text = 'alpha, beta,,,,,gama delta'    # 'alpha', beta,,,,,gama delta
# print(re.split(',', some_text))     # ['alpha', 'beta', 'gama', 'delta'] 表示使用任意个','或者任意个' '来分割字符串
# print(re.split('o(o)', 'fooooobaoor'))    # fooooobaoor--> ['f', 'o', 'ooobaoor'] --> ['f', 'o', '', 'o', 'obaoor'] --> ['f', 'o', '', 'o', 'oba', 'o', 'r']
# print(re.split('o(o)', 'fooooobaoor', maxsplit=2))  # maxsplit表示最多分割的次数

# print(re.findall('[a]', 'abcabc'))    # 以列表形式返回给定模式的所有匹配项
# print(re.sub('name', 'Mrs Liu', 'Dear name...'))    # 替換

# print(re.escape('www.python.org'))
# print(re.escape('But where is the ambiguity?'))     # 将可能被解释为正则运算符的特殊字符转义

# str = 'There (was a (wee) (cooper)) who (lived in Fyfe)'
# 包含的组：
# There (was a (wee) (cooper)) who (lived in Fyfe)
# (was a (wee)
# (cooper))
# (wee)
# (cooper)
# (lived in Fyfe)
# m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())
# print('--------------------')
# print(m.group(1))
# print(m.start(1))
# print(m.end(1))
# print(m.span(1))
#
# print(m.groups())
# print(m.re)
# print(m.string)

# print(re.compile('hello').groups)   # 返回pattern的组数没有组时为0
# \*([^\*]+)\*  匹配任意以单个星号开头，以星号结尾的字符
# emphasis_pattern = re.compile(r'''
# \*          # Beginning emphasis tag -- an asterisk
# (           # Begin group for capturing phrase
# [^\*]+      # Capture anything except asterisks
# )           # End group
# \*          # Ending emphasis tag
# ''', re.VERBOSE)
# print(emphasis_pattern.groups)
# print(re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello, *world!* *python!*'))     # 将*world!*和*python*替换为<em>\1</em>    \1表示pattern中的第一个组

# p = r'\*(.+)\*'     # 默认是贪婪模式
# p = r'\*(.+？)\*'     # 改为非贪婪模式
# print(re.sub(p, r'<>\1<>', '*hello* *world!*'))

# 找出From Foo File <foo@bar.com>中的Foo File
# find_sernder.py
# import fileinput, re
# pat = re.compile('From (.*) <.*?>$')
# for line in fileinput.input():
#     m = pat.match(line)
#     if m:
#         print(m.group(1))
# fileinput.close()

# 找出所有的邮箱
# import fileinput, re
# pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE)
# addresses = set()
# for line in fileinput.input():
#     for address in pat.findall(line):
#         addresses.add(address)
#     if fileinput.isstdin():
#         fileinput.nextfile()
# for address in sorted(addresses):
#     print(address)
# fileinput.close()
from string import Template

Template