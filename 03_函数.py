# -*- coding:utf-8 -*-


def p(a=3, b=2):
    a |= b
    print(a, b)

p()

list1 = [{'a': 1, 'b': 2}, {'a': 11, 'b': 22}]
list2 = [x.get('a') for x in list1]
print(list2)

##结果： [1, 11]


class A:
    def a(self):
        print('A')

class B(A):
    def b(self):
        print('B')

B().a()