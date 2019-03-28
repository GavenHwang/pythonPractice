# -*- coding:utf-8 -*-
from __future__ import division

# Python3 中有六个标准的数据类型：
# Number（数字）：int（python3中没有Long）、float、bool、complex（复数）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）
# Python3 的六个标准数据类型中：
#
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）

# 取整
import datetime
import time
from math import floor

# aa = 1 // 3
# 取余
# bb = 1 % 3
# 乘方
# cc = 2 ** 3

# 判断数据类型
# type()不会认为子类是一种父类类型
# isinstance()会认为子类是一种父类类型
# print(floor(2.9))
#
#
# class A:
#     pass
#
#
# class B(A):
#     pass


# print(isinstance(A(), A))
# True
# print(type(A()) == A)
# True
# print(isinstance(B(), A))
# True
# print(type(B()) == A)
# False

# 在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加
# print(True + False)

# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义
# 字符串可以用+运算符连接在一起，用*运算符重复
# Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始
# str1 = 'Runoob'
# print(str1 * 2)      # 输出字符串两次

# 加号 + 是列表连接运算符，星号 * 是重复操作。如下实例
# list1 = ['abcd', 786, 2.23, 'runoob', 70.2]
# list2 = [123, 'runoob']
# print(list2 * 2)        # 输出两次列表
# print(list1 + list2)    # 连接列表

# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
# set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(a - b)  # a 和 b 的差集
# print(a | b)  # a 和 b 的并集
# print(a & b)  # a 和 b 的交集
# print(a ^ b)  # a 和 b 中不同时存在的元素

# 构造函数 dict() 可以直接从键值对序列中构建字典
# dict1 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# print(dict1)

# 将'3'转换为一个16进制整数
# print(int('3', base=16))

# 将‘12.13’转为浮点型
# float('12.13')

# complex(real [,imag])
# complex(1, 2)   # (1 + 2j)
# complex(1)      # 数字 (1 + 0j)
# complex("1")    # 当做字符串处理 (1 + 0j)
# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
# complex("1+2j")
# (1 + 2j)

# str(x) 将对象 x 转换为字符串

# repr(x)将对象 x 转换为表达式字符串
# dict = {'runoob': 'runoob.com', 'google': 'google.com'}
# repr(dict)      # "{'google': 'google.com', 'runoob': 'runoob.com'}"

# eval(str)用来计算在字符串中的有效Python表达式,并返回一个对象
# eval(expression[, globals[, locals]])
# expression -- 表达式。
# globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
# locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
# eval('pow(2,2)')  # 4

# 快速定义多个变量 globals()    locals()
# for i in range(4):
#     name = 'v' + str(i)
#     globals()[name] = i
# print(v1, v2, v3)

# exec 执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码
# exec("""for i in range(5):
#      print ("iter time: %d" % i)
#  """)
#
# x = 10
# expr = """
# z = 30
# sum = x + y + z
# print(sum)
# """


# def func():
#     y = 20
#     exec(expr)
#     exec(expr, {'x': 1, 'y': 2})
#     exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})
#
# func()


# tuple(s) 将序列 s 转换为一个元组
# list(s) 将序列 s 转换为一个列表
# set(s) 转换为可变集合
# dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。
# frozenset(s) 转换为不可变集合
# chr(x) 将一个整数转换为一个字符
# print(chr(98))  # b
# ord(x) 将一个字符转换为它的整数值
# print(ord('b')) # 98
# hex(x) 将一个整数转换为一个十六进制字符串
# print(hex(255))
# oct(x) 将一个整数转换为一个八进制字符串
# print(oct(255))

# haha01 = [1, 2]
# haha02 = (3, 4, {5: 6})
# haha03 = set([7, 8])
# haha01.extend(haha02)
# haha01.extend(haha03)
# print(haha03)
# print(haha01)

# 字符串格式化
# - 表示左对齐，+ 表示转换之前要加上正负号，“ ” 空白字符表示正数之前保留空格('% d' % 12)，0表示位数不够用0填充
# . 表示精度，转换实数是表示小数点后的位数，转换字符串表示最大宽度
# * 表示字段宽度或者精度
# width = int(input("Please input the Width"))
# price_width = 10
# item_width = width - price_width
# header_format = '%-*s%*s'
# format = '%-*s%*.2f'
# print('=' * width)
# print(header_format % (item_width, "Items", price_width, 'price'))
# print('-'*width)
# print(format % (item_width, 'Apples', price_width, 0.4))
# print(format % (item_width, 'Pears', price_width, 0.5))


from copy import deepcopy
a = [[1, 2, '', '', ['a', 'b']]]
b = deepcopy(a[-1])
a.pop()
for i in range(2):
    b[2] = i
    b[3] = i
    b[4][0]= i
    a.append(b[:])
print(a)

