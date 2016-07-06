#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Author: WangHuafeng

#
# def f1(*args, **kwargs):
#     print(args,type(args))
#     print(kwargs, type(kwargs))
#
# f1(11,22,33,44,'aa',k1='v1',k2='v2')
#
s = "I am {0} , age is {1}".format('wang',20)
s2 = "I am {0} , age is {1}".format(*['wang',20])
s3 = "I am {name} , age is {age}".format(name='wang',age=20)
dic = {'name':'wang','age':20}
s4 = "I am {name} , age is {age}".format(**dic)
print(s4)
