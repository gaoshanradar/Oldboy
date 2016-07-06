#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng


USER_INFO = {}

def check_login(func):
    def inner(*args, **kwargs):
        #.get拿数据时，不存在则默认为None
        if USER_INFO.get('is_login', None):
            ret = func(*args, **kwargs)
            return ret
        else:
            print("请登录！")
    return inner

def check_admin(func):
    def inner(*args, **kwargs):
        if USER_INFO.get('user_type', None) == 2:
            ret = func(*args, **kwargs)
            return ret
        else:
            print("无权限查看！")
    return inner

@check_login
@check_admin
def index():
    """
    管理员的功能
    :return:
    """
    print("Index")

@check_login
def home():
    print("home")

def login():
    user = input("请输入用户名：")
    if user == 'admin':
        USER_INFO['is_login'] = True
        USER_INFO['user_type'] = 2
    else:
        USER_INFO['is_login'] = True
        USER_INFO['user_type'] = 1

def main():
    while True:
        imp = input("1.登录；2.查看信息；3.超级管理员管理 \n >>>")
        if imp == '1':
            login()
        elif imp == '2':
            home()
        elif imp == '3':
            index()

main()