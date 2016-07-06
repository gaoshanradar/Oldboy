#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng


#在函数的外部进行装饰，在不改变调用函数的基础上，可以在执行函数前或执行函数后添加一个功能

def outer(func):
    def inner():
        print('log')
        ret = func()
        print("after")
        return ret
    return inner
    print(123, func)

# @ + 函数名
# 功能：
#       1、自动执行outer函数并且将其下面的函数名f1当作参数传递
#       2、将outer函数的返回值重新赋值给f1
@outer
def f1():
    print("F1")

#执行过程：1.执行outer函数，outer()，并将整体函数f1当作参数传递给outer，即outer(f1)
#           2.打印"123"，并将返回值"123"赋值给f1，即f1 = 123，所以打印f1时，显示123
@outer
def f2():
    print("F2")

@outer
def f100():
    print("F100")