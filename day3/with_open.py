#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng


with open('db') as f:
    pass

#读取db1前10行，然后以只写方式写入db2
with open('db1', 'r', encoding='utf-8') as f1, open("db2", 'w', encoding='utf-8') as f2:
    times = 0
    for line in f1:
        times += 1
        if times <= 10:
            f2.write(line)
        else:
            break

#取一行写一行
with open('db3', 'r', encoding='utf-8') as f3, open("db4", 'w', encoding='utf-8') as f4:
    for line2 in f3:
        new_str = line2.replace("alex", 'steven')
        f2.write(new_str)
