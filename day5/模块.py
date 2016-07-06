#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng


# 先导入后使用，既可以是文件也可以是文件夹
# import lib.commons
# import s3
#
# s3.login()
# s3.logout()
#
# lib.commons.f1()

#创建模块名时，一定不要和内置模块名重名
# import sys
#
# for item in sys.path:
#     print(item)

#不建议import *
#单模块直接import s3
from s3 import login
login()

from lib import commons as lib_commons
from src import commons as src_commons