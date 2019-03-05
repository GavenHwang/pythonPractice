# -*- coding: utf-8 -*-

# def checkIndex(key):
#     if not isinstance(key, int):
#         raise TypeError
#     if key < 0:
#         raise IndexError
#
#
# class ArithmeticSequence:
#     def __init__(self, start=0, step=1):
#         self.start = start
#         self.step = step
#         self.changed = {}
#
#     def __getitem__(self, key):
#         checkIndex(key)
#         try:
#             return self.changed[key]
#         except KeyError:
#             return self.start + key * self.step
#
#     def __setitem__(self, key, value):
#         checkIndex(key)
#         self.changed[key] = value
#
#
# s = ArithmeticSequence(1, 2)
# print(s[4])
# s[4] = 2
# print(s[4])
# print(s['four'])
# print([].__len__())


# class Counterlist(list):
#     def __init__(self, *args):
#         super(Counterlist, self).__init__(*args)
#         self.counter = 0
#
#     def __getitem__(self, index):
#         self.counter += 1
#         return super(Counterlist, self).__getitem__(index)
#
#
# c1 = Counterlist(range(10))
# print(c1)
# c1.reverse()
# print(c1)
# del c1[3:6]
# print(c1)
# print(c1.counter)
# print(c1[2] + c1[4])
# print(c1.counter)


# property函数的__init__方法：__init__(self, fget=None, fset=None, fdel=None, doc=None)
# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#
#     def setSize(self, size):
#         self.width, self.height = size
#
#     def getSize(self):
#         return self.width, self.height
#     size = property(getSize, setSize)
#
#
# r = Rectangle()
# r.width = 10
# r.height = 5
# print(r.size)
# r.size = 150, 100
# print(r.width, r.height)
# 第一个参数是get方法，第二个参数是set方法，第三个参数是delete方法，第四个参数是doc,可以拿java的getName,setName,方法类比
# class C(object):
#     def __init__(self):
#         self._x = None
#
#     def getx(self):
#         return self._x
#
#     def setx(self, value):
#         self._x = value
#
#     def delx(self):
#         del self._x
#
#     x = property(getx, setx, delx, "I'm the 'x' property.")
# c = C()
# c.x = 3
# print(c.x)


# 静态方法和类方法
# class MyClass:
#
#     @staticmethod
#     def smeth():
#         print("This is a static method.")
#     # smeth = staticmethod(smeth)
#
#     @classmethod
#     def cmeth(cls):
#         print("This is a class method of", cls)
#
# a = MyClass()
# a.smeth()
# a.cmeth()


# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#
#     def __setattr__(self, key, value):
#         if key == 'size':
#             self.width, self.height = value
#         else:
#             super(Rectangle, self).__setattr__(key, value)
#
#     def __getattr__(self, item):
#         if item == 'size':
#             return self.width, self.height
#         else:
#             return super(Rectangle, self).__getattr__(item)
#
# a = Rectangle()
# a.size = (10, 15)
# print(a.width, a.height, a.size)

# ********************* 迭代器与生成器 ***************************
# import sys
# # 输出迭代器的下一个元素
# list = [6, 2, 3, 4]
# it = iter(list)
# print(next(it))
#
# # 利用迭代器对象遍历
# list = [1, 2, 3, 5]
# it = iter(list)
# for x in it:
#     print(x, end=" ")
#
#
# # 类实现迭代功能
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
# for x in myiter:
#     print(x, end=' ')
# print()
#
# # 生成器函数 - 斐波那契
# def fibonacci(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()
# 迭代器       python3使用__next__而不是next（）
# class Fibs:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
#     def __iter__(self):
#         return self
#
# f = Fibs()
# for i in f:
#     if i > 1000:
#         print(i)
#         break
#
# lista = [1, 2, 3, 4]
# it = iter(lista)
# # print(next(it))
# print(list(it))
# for i in it:
#     print(i)


# a = [[1,3], [3,4], [5]]
# def fun1():
#     for i in a:
#         for m in i:
#              yield m
# for i in fun1():
#     print(i)

# 生成器
# def flatten(nested):
#     """将列表变为生成器"""
#     try:
#         try:
#             nested + ''
#         except TypeError:
#             pass
#         else:
#             raise TypeError
#         for sublist in nested:
#             for e in flatten(sublist):
#                 yield e
#     except TypeError:
#         yield nested
#
#
# for rec in flatten(['aaa', 'bbb', 'ccc', 'a', 'b', 'c', 1, 2, 3]):
#     print(rec, end=',')

#

# def repeater(value):
#     while True:
#         new = (yield value)
#         if new is not None:
#             value = new
# r = repeater(42)
# print(r.__next__())
# print(r.send("Hello World!"))
# print(r.__next__())

# def flatten(nested):
#     result = []
#     try:
#         try:
#             nested + ''
#         except:
#             pass
#         else:
#             raise TypeError
#         for rec in nested:
#             for e in flatten(rec):
#                 # result.append(e)
#                 yield e
#     except TypeError:
#         # result.append(nested)
#         yield nested
#     return result
#
# print(flatten(['aaa', 'bbb', 'ccc', 'a', 'b', 'c', 1, 2, 3, [4, 5, [6, 7, 8], [9, 10]]]))
# for rec in flatten(['aaa', 'bbb', 'ccc', 'a', 'b', 'c', 1, 2, 3, [4, 5, [6, 7, 8], [9, 10]]]):
#     print(rec, end=',')

# 八皇后问题
# def queen(A, cur=0):
#     """来自百度百科"""
#     if cur == len(A):
#         print(A)
#         return 0
#     for col in range(len(A)):
#         A[cur], flag = col, True
#         for row in range(cur):
#             if A[row] == col or abs(col - A[row]) == cur - row:
#                 flag = False
#                 break
#         if flag:
#             queen(A, cur+1)
# queen([None]*8)

#   # * # #
#   # # # *
#   * # # #
#   # # * #
# 如上图所示，假设不知道第四行皇后的位置，要想找第四行皇后的所有正确的集合
# 1.假设x坐标为 0，遍历前三行的x坐标，不能与0相同，且x坐标差的绝对值不能与y坐标差的绝对值相等（如果相等则在对角线上）
# 1.假设x坐标为 1，遍历前三行的x坐标，不能与0相同，且x坐标差的绝对值不能与y坐标差的绝对值相等（如果相等则在对角线上）
# 1.假设x坐标为 2，遍历前三行的x坐标，不能与0相同，且x坐标差的绝对值不能与y坐标差的绝对值相等（如果相等则在对角线上）
# 1.假设x坐标为 3，遍历前三行的x坐标，不能与0相同，且x坐标差的绝对值不能与y坐标差的绝对值相等（如果相等则在对角线上）
import random


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

def queens(num=4, state=()):
    """打印出所有可能情况"""
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield(pos,) + result

def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * pos + 'X ' + '. ' * (length-pos-1)
    for pos in solution:
        print(line(pos))
prettyprint(random.choice(list(queens(4))))























