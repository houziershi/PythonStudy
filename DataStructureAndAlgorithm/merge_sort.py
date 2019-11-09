#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MergeSort(object):
    def merge_sort(self, a, p, r):
        if p < r:
            q = (r + p) // 2
            # print('q=====', q)
            # self.merge(A, p, q, r)
            self.merge_sort(a, p, q)
            self.merge_sort(a, q + 1, r)
            self.merge(a, p, q, r)

    @staticmethod
    def merge(a, p, q, r):
        m = q - p + 1
        n = r - q

        L = [a[p + i] for i in range(m)]
        print(L)
        R = [a[q + 1 + i] for i in range(n)]
        # print(R)
        x = 0
        y = 0
        for i in range(p, r + 1):
            if x < len(L) and y < len(R):
                if L[x] <= R[y]:
                    a[i] = L[x]
                    x += 1
                    continue
                else:
                    a[i] = R[y]
                    y += 1
                    continue

            if y >= len(R) and x < len(L):
                a[i] = L[x]
                x += 1
                continue
            if x >= len(L) and y < len(R):
                a[i] = R[y]
                y += 1
                continue

    def mergeSort2(self, a):
        current_size = 1

        # Outer loop for traversing Each
        # sub array of current_size
        while current_size < len(a) - 1:

            left = 0
            # Inner loop for merge call
            # in a sub array
            # Each complete Iteration sorts
            # the iterating sub array
            while left < len(a) - 1:
                # mid index = left index of
                # sub array + current sub
                # array size - 1
                mid = left + current_size - 1

                # (False result,True result)
                # [Condition] Can use current_size
                # if 2 * current_size < len(a)-1
                # else len(a)-1
                right = ((2 * current_size + left - 1,
                          len(a) - 1)[2 * current_size
                                      + left - 1 > len(a) - 1])

                # Merge call for each sub array
                self.merge2(a, left, mid, right)
                left = left + current_size * 2

            # Increasing sub array size by
            # multiple of 2
            current_size = 2 * current_size

    # Merge Function
    @staticmethod
    def merge2(a, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2
        for i in range(0, n1):
            L[i] = a[l + i]
        for i in range(0, n2):
            R[i] = a[m + i + 1]

        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            if L[i] > R[j]:
                a[k] = R[j]
                j += 1
            else:
                a[k] = L[i]
                i += 1
            k += 1

        while i < n1:
            a[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            a[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    mergeSort = MergeSort()
    A = [5, 4, 2, 1, 15, 48, 16, 32]
    mergeSort.merge_sort(A, 0, len(A) - 1)
    print("ok")
