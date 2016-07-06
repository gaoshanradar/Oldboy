#！/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: wanghuafeng


# 提示输入用户名和密码
username = input("input your name:")
password = input("input your password:")

#设置登录次数计数器
count = 0

#读取用户信息到变量中
user_info = open("user_name.txt","r")

#循环用户信息
for line in user_info:
    #提取用户名和密码
    line_list = line.strip().split(",")
    #判断用户输入的用户名和密码
    if line_list[0] == username and  line_list[1]== password:
        # 如果一致，打印欢迎信息
        print("Welcome login!")
    else:
        print("用户名密码错误！")
        count += 1
        print("count is : %s" % count)
        if count <= 3:
            print("2.count is : %s" % count)
            username = input("input your name:")
            password = input("input your password:")