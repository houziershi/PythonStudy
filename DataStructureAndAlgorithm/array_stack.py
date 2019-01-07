#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise IndexError('self._data is empty')
        return self._data[-1]


if __name__ == '__main__':
    a= ArrayStack();
    a.push(45)
    a.push(26)
    a.push(14)
    a.pop()
    a.pop()
    a.pop()
    print(a.is_empty())
    print(a.top())