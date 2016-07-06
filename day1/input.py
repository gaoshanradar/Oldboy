#！/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: wanghuafeng

name = input("input your name:")
age = int(input("input your age:"))
job = input("input your job:")
#print("name is:", name + "\nage is:", age + "\njob is:", job)

msg = """
Information of user %s:
-------------------------
Name:    %s
Age :    %d
Job :    %s
---------End-------------
""" % (name, name, age, job)
print(msg)