#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng

"""
def f1():
    pass
#判断函数是否能被调用
print(callable(f1))
"""

#chr()
#ord()
#数字转换为ASCII码
r = chr(65)
print(r)
#ascii转换为数字
n = ord('a')
print(n)

#compile()
#eval()
#exec()

s = "print(123)"
#编译: single(单行), eval（表达式）, exec（编译成和python一样）
#将字符串编译成python代码
r = compile(s, "<string>", "exec")
#执行python代码,没有返回值
exec(r)

#eval只执行表达式有返回结果
box = "8 * 8"
ret = eval(box)
print(ret)

#dir()查看一个对象提供的功能
dir(dict)
#查看功能的具体使用，即源码
help(list)
#divmod()
#共97条数据，每页显示10条，需要多少页？
n1, n2 = divmod(97,10)
#n1为商，n2位=为余数
print(n1, n2)

#对象：由类创建，对象是类的实例
a = "wang"
#判断对象是否是类的实例
r = isinstance(a, str)
print(r)

#filter()筛选符合条件的函数
list_filter = [21,22,33,44,5,66,777,88,9,0,89]
def f2(a):
    if a > 22:
        return True
#filter(函数,可迭代的对象),filter内部首先会循环第二个参数，将每一个循环元素取去执行第一个参数（即函数）
# 如果函数返回True,将元素添加到结果中
ret = filter(f2, list_filter)
print(list(ret))

#自动return
f1 = lambda a: a > 30
ret = f1(31)
print(ret)

li = [11,22,33,44,55,66]
result = filter(lambda a: a > 33, li)
print(list(result))

#map（函数，可迭代的对象（可以for循环的内容））
# 将返回值添加到结果中
li = [11,22,33,44,55,66]
result = map(lambda a: a + 100, li)
print(list(result))

#globals()所有的全局变量
#locals()

NAME = 'alex'

def show():
    a = 123
    print(locals())
    print(globals())
show()
#hash()用于字典的key保存
s = 'pssiacmaakmcasmcamcasomcwmclwmclw'
print(hash(s))

#id()查看内存地址
#iter()创建迭代器
#len()查看长度
s = "哈哈"
b = bytes(s, encoding='utf-8')
#python3.*即可通过字符查看，也可以通过字节查看
#python2.7只能通过字节查看
print(len(b))
ss = "哈哈"
for a in ss:
    print(a)

#max(),min(),sum()
rr = max([11,22,33,44])
print(rr)
aa = min([11,22,33,44])
print(aa)
dd = sum([11,22,33,44])
print(dd)

#object是所有类的父类
#pow()求指数
r6 = pow(2, 10)
print(r6)
#round()四舍五入
r = round(4.6)
print(r)
#slice()切片
#sort()排序
#vars()查看变量
#zip()

li = [11, 22, 33, 44, 'll']
li.reverse()
l1 = ['alex', 11, 22 ,33]
l2 = ['is', 11, 22, 33]
l3 = ['sb', 11, 22, 33]

r = zip(l1, l2, l3)
temp = list(r)[0]
ret = ' '.join(temp)
print(ret)