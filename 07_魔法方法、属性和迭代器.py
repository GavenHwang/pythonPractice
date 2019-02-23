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


a = [[1,3], [3,4], [5]]
def fun1():
    for i in a:
        for m in i:
             yield m
for i in fun1():
    print(i)

























