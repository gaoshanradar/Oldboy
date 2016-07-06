#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng


def outer(func):
    def inner(*args, **kwargs):
        print("before")
        #如果原函数有返回值需要在装饰器函数中添加返回
        r = func(*args, **kwargs)
        print("after")
        #将原函数中的返回值返回
        return r
    return inner

@outer
def f1(arg):
    print(arg)
    return "haha"

@outer
def f2(arg1, arg2):
    print("F2")

