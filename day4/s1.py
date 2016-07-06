#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng


def f1():
    print('123')

#xxx代指函数f1()整体，函数整体可以当作参数传递
def f2(xxx):
    xxx()

f2(f1)