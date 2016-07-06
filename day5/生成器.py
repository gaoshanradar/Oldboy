#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng


#生成器，使用函数创造
#普通函数
# def func():
#     return 123
#
# ret = func()

# li = [11, 22, 33, 44]
# result = filter(lambda x:x>22, li)
# #具有生成指定条件数据能力的一个对象，只有循环时才生成
# print(result)

#普通函数中出现yield则称之为生成器
# def func():
#     yield 1
#     yield 2
#     yield 3
#
# ret = func()
# #
# # for i in ret:
# #     print(i)
#
# r1 = ret.__next__() #进入函数找到yield，获取yield后面的数据
# print(r1)
# r2 = ret.__next__() #进入函数找到yield，获取yield后面的数据
# print(r2)
# r3 = ret.__next__() #进入函数找到yield，获取yield后面的数据
# print(r3)


def myrange(arg):
    start = 0
    while True:
        if start > arg:
            return
        yield start
        start += 1

ret = myrange(3)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)