#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng
#open打开文件乱码，查看文件保存模式
#平时都使用UTF-8编码方式
f = open('db','r', encoding="GBK")
data = f.read()
print(data, type(data))
f.close()

#f = open('db','rb')直接使用二进制编码
f = open('db','rb')
data1 = f.read()
print(data1, type(data1))
f.close()

f = open('db','ab')
f.write(bytes("雪雪", encoding="utf-8"))
f.close()