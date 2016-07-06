#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng

#1. %s %d
#2. forrmat
'''
a = "I am {0}, age{1}".format("wang", 19)
b = "I am {0}, age{1}".format(*["wang", 19])
print(a)
print(b)
'''

c1 = "I am {name}, age is {age}".format(age=18, name="wang")
print(c1)
dict_name = {'name':'wang', 'age':22}
c2 = "I am {name}, age is {age}".format(**dict_name)
print(c2)