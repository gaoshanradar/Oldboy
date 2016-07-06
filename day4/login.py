#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng


#装饰器做权限认证
LOGIN_USER = {"is login" : False}

def outer(func):
    def inner(*args, **kwargs):
        if LOGIN_USER['is login']:
            r = func(*args, **kwargs)
            return r
        else:
            print("请登录")

@outer
def manager():
    print("欢迎%s登录" % LOGIN_USER['current_user'])

def login(user, pwd):
    if user == "alex" and pwd == '123':
        LOGIN_USER['is login'] = True
        LOGIN_USER['current_user'] = user
        manager()


def main():
    inp = input("1.后台管理；2.登录")
    if inp == '1':
        manager()
    elif inp == '2':
        username = input("请输入用户名：")
        pwd = input("请输入密码：")
        login(username, pwd)

main()