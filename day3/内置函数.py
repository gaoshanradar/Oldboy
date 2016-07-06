#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng

#取绝对值
n = abs(-1001)
print(n)
# 0 None 空字符串 空列表 空字典 空元组 bool值都是False
print(bool(0))
#所有为真才为真
n = all([1,2,3,0])
print(n)
#只要有真就为真
n = any([0,1,0,0,0])
print(n)
#自动执行对象的__str__方法
class Foo:
    def __repr__(self):
        return "65"
n = ascii(Foo())
print(n)

#bin() 二进制
print(bin(23))
#oct() 八进制
print(oct(345))
#hex() 十六进制
print(hex(1111111))


#bytes(),汉字utf-8编码3个字节，GBK一个汉字两个字节，一个字节8位
s = "二万画画"
# 01000110 01000110 01000110 01000110 01000110 01000110 01000110 01000110 01000110 01000110 01000110 01000110
# 43        43          43      43      43      43      43          43      43      43          43      43
#字符串转字节
#bytes(待转换的字符串, 按照什么编码)
m = bytes(s, encoding="utf-8")
m1 = bytes(s, encoding="GBK")
print(m)
print(m1)
m2 = bytearray(s, encoding="utf-8")
print(m2)

#字节转换为字符串,编码方式保持一致
m3 = str(m2,encoding="utf-8")
print(m3)

#文件操作open
#1.打开文件
f = open('db','r')  #只读
f = open('db','w')  #只写，写之前清空文件
f = open('db','x')  #文件存在就报错；不存在创建并只写
f = open('db','a')  #追加

#2.操作文件
f.read()
f.readlines()
f.readline()
#3.关闭文件
f.close()

with open('db') as f:
    pass