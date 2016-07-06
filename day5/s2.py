#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng
#开放、封闭原则：对函数内部封闭，对函数外部开放
#不改变原函数的基础上，在它之前或之后做一些别的操作

def outer(func):
    def inner(*args, **kwargs):
        print("before")
        r = func(*args, **kwargs)
        print("after")
        return r
    return inner


#自动执行outer函数，并将其下面的函数名f1当作参数传递
#将outer函数的返回值重复赋给f1
@outer
def f1(arg):
    print(arg)
    return "你好"

@outer
def f2(arg1, arg2):
    print("f2")

@outer
def f100():
    print("f100")

