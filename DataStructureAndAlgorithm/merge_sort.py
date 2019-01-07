#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MergeSort(object):
    def merge_sort(self, a, p, r):
        if p < r:
            q = (r + p) // 2
            print('q=====', q)
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
        print(R)
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


if __name__ == '__main__':
    mergeSort = MergeSort();
    A = [5, 4, 2, 1, 15, 48, 16, 32]
    mergeSort.merge_sort(A, 0, len(A) - 1)
    print("ok")
