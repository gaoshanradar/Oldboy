#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Author: WangHuafeng



#set特性：无序，不重复，可嵌套
# 创建set

#list()相当于执行构造方法__int__，内部会执行一个for循环，循环(11,22,33,44,11,22,33)set差异
s1 = {11, 33, 44, 66}
s2 = {22, 33, 44 ,55, 88}
s1.update((11,22,33,44,55,66,77,88,99,00))
print(s1)

