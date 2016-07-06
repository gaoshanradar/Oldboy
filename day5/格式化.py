#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng

s = "My name is %(name)s ,age is %(age)d" %{'name':'wang', 'age':29}
print(s)

s1 = "My name is %(name)+10s ,age is %(age)+10d" %{'name':'wang', 'age':29}
print(s1)

s2 = "My nameis%(name)-10s ,age is %(age)-10d" %{'name':'wang', 'age':-29}
print(s2)
s3 = "My name is %(name)s ,age is %(age)d" %{'name':'wang', 'age':29}
print(s3)

s4 = "My name is %(name)s ,age is %(age)x %(p).2f" %{'name':'wang', 'age':29, 'p':1.234567}
print(s4)

s5 = "My name is %(name)s ,age is %(age)c %(p).2f" %{'name':'wang', 'age':67, 'p':1.234567}
print(s5)

#当格式化时，字符串中出现占位符%s,%d时，必须使用%%才能显示一个%，即转义
s6 = "wang %s %%" %('haha')
print(s6)

s7 = "aasasasasa{0}as23456{1}".format(123,'qqq')
print(s7)

s8 = "------{name:s}___________{age:d} ========={name:s}".format(name='wang', age=29)
print(s8)
s9 = "----------{:0^20s}===={:+d}-------{:#b}".format('wang', 12345, 18)
print(s9)