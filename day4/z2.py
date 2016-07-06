#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng


import s2

# f1被装饰器装饰后返回值为None，如果原函数有返回值需要在装饰器函数中添加返回
ret = s2.f1("fish")
print(ret)
s2.f2("haha", "niu")
