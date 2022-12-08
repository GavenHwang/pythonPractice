# -*- coding:utf-8 -*-
import copy
from itertools import permutations, combinations


def jiu_X_jiu():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%sX%s=%s\t' % (j, i, j * i), end='')
        print()


# jiu_X_jiu()


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    print(array)


# bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])


def select_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]
    print(array)


# select_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])


def combine(lst, l):
    result = []
    tmp = [0] * l

    def next_num(i, n):
        if n == l:
            result.append(tmp[:])
            return
        for j in range(i, len(lst)):
            tmp[n] = lst[j]
            next_num(j + 1, n + 1)

    next_num(0, 0)
    return result


print("手写实现组合", combine([1, 2, 3, 4, 5], 2))
print("内置组合函数", list(combinations([1, 2, 3, 4, 5], 2)))


def permutation(lst, l):
    result = []
    tmp = [0] * l

    def next_num(arr, n):
        if n == l:
            result.append(tmp[:])
            return
        for i in arr:
            tmp[n] = i
            b = arr[:]
            b.pop(arr.index(i))
            next_num(b, n + 1)

    c = lst[:]
    next_num(c, 0)
    return result


print("手写实现排列", permutation([1, 2, 3, 4, 5], 2))
print("内置函数排列", list(permutations([1, 2, 3, 4, 5], 2)))

print(bin(12))
print(oct(12))
print(int(12))
print(hex(12))