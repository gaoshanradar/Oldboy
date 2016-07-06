#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng
#python规定：如果对某个参数默认值，必须将其放到末尾
def sendmail(em, content, mm = "OK"):
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    try:
        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["王华峰",'18700821967@163.com'])
        msg['To'] = formataddr(["学习Python函数部分",em])
        msg['Subject'] = "学习Python函数部分发送邮件"

        #开启smtp服务，并输入用户名、密码
        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("18700821967@163.com", "12#qazwe")
        server.sendmail('18700821967@163.com', [em,], msg.as_string())
        server.quit()
    except:
        #发送失败
        return False
    else:
        #发送成功
        return True
        #return cc

while True:
    #实际参数
    em = input("请输入邮箱地址：")
    result = sendmail(em, 'haha')
    #指定参数
    #result = sendmail(content ='haha', em, mm = "SS")
    if result == True:  # 也可以判断cc
        print("邮件发送成功！")
    else:
        print("邮件发送失败！")