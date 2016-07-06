#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng

#s = "[11, 22, 33, 44]"
"""s = '{"k1":"v1"}'
print(type(s), s)
import json
n = json.loads(s)   #将一个字符串转换成python的基本数据类型，注意：字符串形式的字典'{"k1":"v1"}'内部的字符串必须为双引号
print(type(n), n)
"""
import json
r = '''
{"backend":"www.oldboy.org", "record":
{"server":"100.1.7.9","server":"100.1.7.19","weight":20, "maxconn":3000}}
'''
dic = json.loads(r)
bk = dic['backend']
print(bk)
rd = "server %s %s weight %d maxconn %d" %(dic['record']['server'],
                                           dic['record']['server'],
                                           dic['record']['weight'],
                                           dic['record']['maxconn'])

print(rd)
#print(type(r), r)
