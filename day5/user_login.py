#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng
#最常用的功能是做权限的认证

LOGIN_USER = {"is_login": False}

def outer(func):
    def inner(*args, **kwargs):
        if LOGIN_USER['is_login']:
            r = func()
            return r
        else:
            print("请登录")
    return inner

@outer
def order():
    print("欢迎%s登录" % LOGIN_USER['current_user'])

@outer
def changepwd():
    print("欢迎%s登录" % LOGIN_USER['current_user'])

@outer
def manager():
    print("欢迎%s登录" % LOGIN_USER['current_user'])

def login(user, pwd):
    if user == "alex" and pwd == "123":
        LOGIN_USER['is_login'] = True
        LOGIN_USER['current_user'] = user
        manager()

def main():
    while True:
        inp = input("1.后台管理； 2.登录")
        if inp == '1':
            manager()
        elif inp == '2':
            username = input("请输入用户名：")
            pwd = input("请输入密码：")
            login(username, pwd)

main()