#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Pizza(object):
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


print(Pizza(42).get_size())
