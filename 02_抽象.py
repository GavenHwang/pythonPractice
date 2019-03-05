# -*- coding: utf-8 -*-

# def p(a=3, b=2):
#     a |= b
#     print(a, b)
#
# p()
#
# list1 = [{'a': 1, 'b': 2}, {'a': 11, 'b': 22}]
# list2 = [x.get('a') for x in list1]
# print(list2)
#
# ##结果： [1, 11]
#
#
# class A:
#     def a(self):
#         print('A')
#
# class B(A):
#     def b(self):
#         print('B')
#
# B().a()

# 斐波那契数列
# def fun_fibs(num):
#     """输出斐波那契数列的前num项"""
#     fibs = [0, 1]
#     for i in range(num - 2):
#         fibs.append(fibs[-2] + fibs[-1])
#     print(fibs)


# fun_fibs(8)


# 判断是否可调用
# import math
# x = 1
# y = math.sqrt
# print(callable(x))
# print(callable(y))


# 文档化函数
# from math import sqrt
# print(sqrt.__doc__)
# print(fun_fibs.__doc__)
# help(fun_fibs)


# 理解局部变量
# def rename(name):
#     name = 'rename'
# name = 'name'
# rename(name)
# print(name)

# def relist(a):
#     a[0] = 'a'
# a = ['aa', 'bb']
# # relist(a)
# # print(a)
# relist(a[:])
# print(a)

# 关键字参数
# 收集参数
# def story(**args):
#     return 'Once upon a time, there was a %(job)s called %(name)s.' % args
#
#
# def power(x, y, *args):
#     if args:
#         print('Received redundant parameters:', args)
#     return pow(x, y)
#
#
# def interval(start, stop=None, step=1):
#     'Imitates range() for step > 0'
#     if stop is None:
#         start, stop = 0, start
#     result = []
#     i = start
#     while i < stop:
#         result.append(i)
#         i += step
#     return result
#
#
# print(story(job='king', name='Gumby'))
# print(story(name='gaven', job='brave knight'))
# params = {'job': "language", 'name': 'python'}
# print(story(**params))
# del params['job']
# print(story(job='stroke of genius', **params))
# print(power(2, 3))
# print(power(3, 2))
# print(power(y=3, x=2))
# params = (5,) * 2
# print(params)
# print(power(*params))
# print(power(3, 3, 'hello, world'))
# print(interval(10))
# print(interval(1, 5))
# print(interval(3, 12, 4))
# print(power(*interval(3, 7)))


# 作用域
# x = 1
# scope = vars()
# print(scope.get('x'))


# 闭包
# def out(o):
#     def inner(i):
#         print(o * i)
#     return inner
# a = out(2)
# a(3)


# 阶乘
# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n - 1)
# print(fac(3))


# 幂
# def power(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * power(x, n-1)
# print(pow(2, 3))


# 二分查找
# def search(sequence, number, lower, upper):
#     if lower == upper:
#         return 'index of %s is: %s' % (number, lower)
#     else:
#         middle = (lower + upper) // 2
#         if number > sequence[middle]:
#             return search(sequence, number, middle + 1, upper)
#         else:
#             return search(sequence, number, lower, middle)
# a = [1, 2, 3, 4]
# print(search(a, 3, 0, len(a)-1))

# map
# a = (1, 2, 3)
# for i in map(int, a):
#     print(i)

# filter
# def func(x):
#     return x.isalnum()
# a = ['##$', '~!', 'a1', 'b2']
# for i in filter(func, a):
#     print(i)
# filter(lambda x: x.isalnum(), a)

# reduce
from functools import reduce

a = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x+y, a))