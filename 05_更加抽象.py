# -*- coding: utf-8 -*-

# class A:
#     c = 'cc'
#     __d = 'dd'
#
#     def __aa(self):
#         print('aa')
#
#     def bb(self):
#         print('bb')
#
# a = A()
# print(a._A__d)

# def foo(x): return x*x
# foo = lambda x: x*x
# print(foo(4))
# print(foo)
# def haha():
#     print('haha')
# class A:
#     def a(self):
#         print('a')
#
# class B(A):
#     def a(self):
#         print('a-b')
#     def b(self):
#         print('b')
#
# a = A()
# b = B()
#
# # __bases__ 用于查看类的基类
# print(A.__bases__, B.__bases__)
# # isinstance用于检验对象是否是类的实例
# print(isinstance(a, A), isinstance(b, A))
# # 查看对象所属的类
# print(a.__class__, b.__class__)
# print(type(a), type(b))
# print(hasattr(a, 'a'))
# print(callable(getattr(a, 'a', None)))
# # 设置对象属性
# setattr(a, 'haha', haha)
# a.haha()


# class A:
#     def a(self):
#         print('a')
#
# class B:
#     def a(self):
#         print('b')
#
# class C(A, B):
#     pass
#
# c = C()
# # A中的a方法，重写了B中的a方法（先继承的类中的方法，会重写后继承的类中的方法）
# c.a()
