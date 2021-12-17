# -*- coding:utf-8 -*-


def jiu_X_jiu():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%sX%s=%s\t' % (j, i, j * i), end='')
        print()


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)


def select_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]
    print(array)


if __name__ == '__main__':
    jiu_X_jiu()
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    # bubble_sort(array)
    select_sort(array)