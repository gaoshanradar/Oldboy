#！/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: wanghuafeng

user = 'wanghuafeng'
passwd = '123456'

username = input("input your name:")
password = input("input your password:")

if user == username and passwd == password:
    print("Welcome to login...")
else:
    print("用户名或密码错误...")
