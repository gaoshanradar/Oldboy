#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng

#1.关键字def，创建函数
#2.函数名
#3.()
#4.函数体
'''
def sendmail():
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    try:
        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["王华峰",'18700821967@163.com'])
        msg['To'] = formataddr(["学习Python函数部分",'gaoshanshangdeyu@163.com'])
        msg['Subject'] = "学习Python函数部分发送邮件"

        #开启smtp服务，并输入用户名、密码
        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("18700821967@163.com", "12#qazwe")
        server.sendmail('18700821967@163.com', ['gaoshanshangdeyu@163.com',], msg.as_string())
        server.quit()
    except:
        #发送失败
        return False
    else:
        #发送成功
        return True
        #return cc
ret = sendmail()
print(ret)
if ret == True: #也可以判断cc
    print("邮件发送成功！")
else:
    print("邮件发送失败！")
'''
#在函数中只要执行return，后续的代码都不会执行
def f1():
    print(123)
    return "111"
    print(234)
r = f1()
print(r)

#如果没有return会默认返回一个值None
def f2():
    print(12345)
r2 = f2()
print(r2)
