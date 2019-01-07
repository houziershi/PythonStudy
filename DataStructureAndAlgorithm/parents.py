#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from DataStructureAndAlgorithm.ancestor import Ancestor


class Parent(Ancestor):
    def parents_method(self):
        print('parents method')


if __name__ == "__main__":
    p = Parent()
    p.ancestor_method()
