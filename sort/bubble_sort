#!/usr/bin/env/python
# coding=utf-8

from utils.timer import timer


@timer
def bubble_sort(arr):
    """
    冒泡排序
    """
    count = len(arr)
    for i in range(count):
        for j in range(i+1, count):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == '__main__':
    test_arr = [5, 6, 1, 8, 3, 0, 91, 51, 64, 78, 30, 16, 76, 31, 46, 469]
    bubble_sort(test_arr)
    print(test_arr)
