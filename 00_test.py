# -*- coding: utf-8 -*-


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