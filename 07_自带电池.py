# -*- coding: utf-8 -*-

import sys
# sys.path.append('D:/Users/Gaven/PycharmProjects/PythonPractice/hello.py')
# sys.path.remove('D:/Users/Gaven/PycharmProjects/PythonPractice/hello.py')
#
# import hello
# import hello
# import两次hello但只会打印出一次“Hello World!”,也就是说模块在第一次导入到程序中时被执行,这样可以避免重复载入
# import hello
# hello.hello()
# hello.test()

# import sys, pprint
#
# 让sys.path本身包含正确目录的两种方法：
# 1. 将模块放在正确的位置：sys.path 所输出的位置
# ppprint:智能打印输出
# pprint.pprint(sys.path)

# 2.告诉程序应该去哪儿里找
# 增加环境变量 PYTHONPATH
# print(sys.prefix)

# 包
# import drawing
# from drawing import shape
#
# shape.shape()
# drawing.colors.colors()

import copy

print(dir(copy))
print([n for n in dir(copy) if not n.startswith("_")])
print(copy.__all__)
print("----------------------------")
help(copy.copy)
print("----------------------------")
print(range.__doc__)
print("----------------------------")
print(copy.__file__)