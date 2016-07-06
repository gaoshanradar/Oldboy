#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng
# 创建两个相同函数，以后面创建的函数为准，前面创建的废弃
def f1(a1, a2):
    return a1 + a2

def f1(a1, a2):
    return a1 * a2

ret = f1(8, 8)
print(ret)  #64

#函数的参数在传递时时引用还是值？答案是引用。
def f2(a3):
    a3.append(999)
li = [11,22,33,44]
f2(li)
print(li)   #[11, 22, 33, 44, 999]

#全局变量：所有的作用域里都可读；
# 优先使用自己定义的变量;
# global name3进行重新赋值
# 特殊：列表和字典，可修改不可重新赋值
# 全局变量一定要全部大写

NAME3 = "alex"
def f3():
    global NAME3
    NAME3 = "wang"
    print(NAME3)
def f4():
    print(NAME3)
f3()
f4()

NAME4 = [11,22,33,44,55]
def f5():
    print(NAME4)
    NAME4.append(66)
def f6():
    print(NAME4)

f5()
f6()