#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Author: WangHuafeng

x = 12
def f():
    global x
    x += 2

f()
print(x)
