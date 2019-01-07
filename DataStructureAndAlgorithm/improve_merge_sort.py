#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import traceback


def merge_sort(arr):
    print('merge_sort enter')
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[mid:]), merge_sort(arr[:mid])
    print('merge_sort end')
    return merge(left, right)


def merge(left, right):
    #traceback.print_stack()
    print('--111111------merge enter','  left =',left, '   -------right=',right,'-----------')
    arr = []
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] < right[right_cursor]:
            arr.append(left[left_cursor])
            left_cursor += 1
        else:
            arr.append(right[right_cursor])
            right_cursor += 1

    for i in range(left_cursor, len(left)):
        arr.append(left[i])

    for j in range(right_cursor, len(right)):
        arr.append(right[j])
    print(' 22222merge end arr = ',arr)
    return arr


if __name__ == '__main__':
    A = [5, 4, 3, 2, 1]
    print(merge_sort(A))
    print([None]*10)
