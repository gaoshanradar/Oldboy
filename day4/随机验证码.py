#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng

import random
list_temp =[]
for i in range(10):
    r = random.randrange(0,10)
    if r == 2 or r == 4 or r == 9:
        num = random.randrange(0, 10)
        list_temp.append(str(num))
    else:
        temp = random.randrange(65, 91)
        c = chr(temp)
        list_temp.append(c)
result = "".join(list_temp)
print(result)