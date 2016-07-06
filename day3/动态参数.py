#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng
# *默认传值，传什么接收什么
# ** 指定key、value
#动态参数，直接放入元组中,如果传入列表，则将列表转换为元组的一个元素
#1.普通参数（严格按照顺序，将实际参数赋值给形式参数）
#2.默认参数（必须放置在参数列表的最后）
#3.指定参数（将实际参数赋值给指定的形式参数）
#4.动态参数：
#           *       默认将传入传入的参数，全部放置在元组中，f1(*[11,22,33,44])
#           **      默认将传入的参数，全部放置在字典中，f2(**{'k1':'v1','k2':'v2'})
#5.万能参数：        *args, **kwargs

def f1(*args):
    print(args, type(args))
f1(11,22,33)
li = [11,22,33,"ee"]
f1(li, 888)
#加*将列表中的每一个元素转化到元组中
f1(*li)
al = "wang"
f1(*al)

#加两个*,为字典，指定key和value
def f2(**args):
    print(args, type(args))
f2(nn = "wanghuafeng")
f2(ni = "wang", n2 = 22)

dic = {'k1': 'v1', 'k2':'v2'}
f2(kk = dic)
#{'kk': {'k2': 'v2', 'k1': 'v1'}} <class 'dict'>
f2(**dic)
#{'k2': 'v2', 'k1': 'v1'} <class 'dict'>

#万能参数
#*在前面，**在后面
def f3(*args, **kwargs):
    print(args)
    print(kwargs)
f3(11,22,33,44, k1 = "v1", k2 = "v2")