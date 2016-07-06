#！/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: wanghuafeng

user = 'wanghuafeng'
passwd = '123456'

username = input("input your name:")
password = input("input your password:")

if user == username:
    print("username is correct...")
    if passwd == password:
        print("Welcome to login...")
    else:
        print("password is invalid...")
else:
    print("username is invalid...")