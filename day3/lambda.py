#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng

def f1(a1):
    return a1 + 100
ret1 = f1(10)
print(ret1)

#定义函数f2，冒号前面的为参数，冒号后面为表达式，隐含return功能,只能写一行，会返回结果
f2 = lambda a1, a2: a1 + 100 + a2
ret2 = f2(9,10)
print(ret2)