#! usr/bin/env python3
# -*- coding:utf-8 -*-


def variable_arg(a, b, *l):
    """可变参数"""
    return a + b + sum(l)


def key_word_arg(name, age, **key):
    """关键字参数"""
    print(name, age, 'other ===', key)


def named_keyword_arg_1(name, age, *, city, job):
    """命名关键字参数形式1"""
    print(name, age, city, job)


def named_keyword_arg_2(name, age, *args, city, job):
    """"命名关键字参数形式2: 可变参数"""
    print(name, age, "other=", args, city, job)


if __name__ == '__main__':
    print(variable_arg(10, 12, *[1, 2, 8]))
    key_word_arg('guokun', '66666', city='beijing')
    named_keyword_arg_1('guokun', 12, city='beijing', job='Internet')
    named_keyword_arg_2('guokun', 12, *[1, 2, 3], city='beijing', job='Internet')
