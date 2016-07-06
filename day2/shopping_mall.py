#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng

#输入工资一次性
salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
else:
    exit("Invalid date type...")

welcome_msg = 'Welcome to Wang Shopping mall.'.center(50,'-')
print(welcome_msg)

product_list = [
    ('iphone', 5800),
    ('Mac Air', 8000),
    ('xiaomi', 19.9),
    ('coffee', 30),
    ('Tesla', 820000),
    ('Bike', 900),
]
exit_flag = False
print("Product list.".center(50,'-'))
shop_car = []
while not exit_flag:    #while exit_flag is not True
    for item in enumerate(product_list):    #enumerate枚举
        #p_name, p_price = product_item
        #print(p_name, p_price)
        #print(item)
        index = item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print(index,'.',p_name,p_price)

    user_choice = input("[q=quit,c=check]What do you want to buy : ")
    if user_choice.isdigit():   #肯定选择shopping
        user_choice = int(user_choice)
        if user_choice < len(product_list):
            p_item = product_list[user_choice]
            if p_item[1] <= salary: #买得起
                shop_car.append(p_item) #加入购物车
                salary -= p_item[1] #扣钱
                print("Added [%s] into shop car,you current balance is \033[31;1m][%s]\033[0m" % (p_item, salary))
            else:
                print("Your balance is [%s], cannot afford this." % salary)
    else:
        if user_choice == 'q' or user_choice == 'quit':
            print("purchased products as below".center(40,'*'))
            for item in shop_car:   #打印已购买的商品
                print(item)
            print("END".center(40,'*'))
            print("Your balance is \033[41;1m][%s]\033[0m" % salary)
            print("Bye")
            exit_flag = True
        elif user_choice == 'c' or user_choice == 'check':
            print("purchased products as below".center(40, '*'))
            for item in shop_car:  # 打印已购买的商品
                print(item)
            print("END".center(40, '*'))
            print("Your balance is [%s]" % salary)