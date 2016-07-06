#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng
#r+:即可读又可写，需要找到指针的位置
f = open('db', 'r+', encoding="utf-8")
#如果打开模式没有b，则read按照字符读取
data = f.read(3)
# tell当前指针所在的位置（字节）
print(f.tell())
# 调整写入指针位置（字节）
f.seek(f.tell())
# 当前指针位置开始覆盖写入
f.write("admin")
f.close()

"""
打开文件的模式有：

r ，只读模式【默认】
w，只写模式【不可读；不存在则创建；存在则清空内容；】
x， 只写模式【不可读；不存在则创建，存在则报错】
a， 追加模式【可读；   不存在则创建；存在则只追加内容；】
"+" 表示可以同时读写某个文件

r+， 读写【可读，可写】
w+，写读【可读，可写】
x+ ，写读【可读，可写】
a+， 写读【可读，可写】
 "b"表示以字节的方式操作

rb  或 r+b
wb 或 w+b
xb 或 w+b
ab 或 a+b
 注：以b方式打开时，读取到的内容是字节类型，写入时也需要提供字节类型
fileno文件描述符
flush刷新
readline仅读取一行
truncate截断，指针位置后面的内容清空
f = open('db','r+',encoding = 'utf-8')
for line in f:
    print(line)

关闭文件
f.close
with open('xb') as f:
    pass
"""