#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Author: WangHuafeng


salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
else:
    exit("Invalid date type...")

welcome_msg = 'Welcome to Wang Shopping Mall'.center(50,'-')
print(welcome_msg)

product_list = [
    ('iphone', 5800),
    ('Mac Air', 8000),
    ('Mac pro', 18000),
    ('xiaomi', 19.9),
    ('coffee', 30),
    ('Tesla', 820000),
    ('Bike', 900),
    ('Cloth', 500),
]
shop_car = []
exit_flag = False
while not exit_flag:
    print("Product list".center(50,'-'))
    for item in enumerate(product_list):
        index = item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print(index, '.', p_name, p_price)
    user_choice = input("[q=quit,c=check]What do you want to buy?：")
    #检测长度
    if user_choice.isdigit():
        user_choice = int(user_choice)
        #不能超过商品列表长度
        if user_choice < len(product_list):
            #购买商品数量
            p_number = input("Input product number :")
            if p_number.isdigit():
                p_number = int(p_number)
            else:
                exit("Invalid date type...")
            p_item = product_list[user_choice]
            p_total = p_item[1]*p_number
            if p_total <= salary:
                #放入购物车
                shop_car.append(p_number*p_item)
                #扣款
                salary -= p_total
                print("Added %s [%s] into shop car,you current balance is \033[31;1m[%s]\033[0m" % (p_number, p_item, salary))
            else:
                print("Your balance is \032[31;1m[%s]\032[0m, cannot afford this." % salary)
    else:
        if user_choice == 'q' or user_choice == 'quit':
            print("purchased product as below:".center(40,'*'))
            for item in shop_car:
                print(item)
            print("Bye".center(40,'*'))
            print("Your balance is [%s]" % salary)
            exit_flag = True
        elif user_choice == 'c' or user_choice == 'check':
            print("purchased products as below".center(40, '*'))
            for item in shop_car:  # 打印已购买的商品
                print(item)
            print("END".center(40, '*'))
            print("Your balance is [%s]" % salary)