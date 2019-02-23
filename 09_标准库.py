# -*- coding: utf-8 -*-
import pprint
import sys

# ********************* SYS ***************************
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
# fileinput.nextfile()        # 关闭当前文件，移动到下一个文件
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

import time

# time.asctime()    将时间元组转换为字符串, 默认为当前时间    Fri Feb 22 17:40:51 2019
# print(time.asctime() + '')
# print(time.asctime(time.localtime()))
# time.localtime()  将秒数转化为日期元组，以本地时间为准  time.struct_time(tm_year=2019, tm_mon=2, tm_mday=22, tm_hour=17, tm_min=40, tm_sec=22, tm_wday=4, tm_yday=53, tm_isdst=0)
# print(time.localtime(time.time()))
# time.mktime()     将时间元组转换为本地时间
# print(time.mktime(time.localtime()))
# time.sleep()      休眠
# time.strftime()   将字符串解析为时间元组
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
time_str = time.strftime("%Y-%m-%d", time.localtime())
print(time.mktime(time.strptime(time_str, "%Y-%m-%d")))

# a = "Sat Mar 28 22:24:24 2016"
# print(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
# print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
# time.time()       当前时间