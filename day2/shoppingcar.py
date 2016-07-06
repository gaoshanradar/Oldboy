#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Author: WangHuafeng


product_list = [
    ("iPhone6s",5699),
    ("Mac Pro",15888),
    ("Kindle",499),
    ("零基础学Python",49),
    ("Apple",10)
]

user_asset = input('please input your asset:')
break_flag = False
shopping_car = []
paid_list = []

while not break_flag:
    for index,i in enumerate(product_list,1):
        print(index,i[0],i[1])
    user_choice = input("What do you want to buy?[quit/check/pay]")

    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice < len(product_list) and user_choice > 0:
            shopping_car.append(product_list[user_choice-1])
            print("Just has added [%s] in your shopping car." % shopping_car)
        else:
            print("Wrong input,please input again.")
    elif user_choice == "check":
        total_price = 0
        print("You have bought below products.")

        for index,p in enumerate(shopping_car,1):
            print(index,p)
            total_price += p[1]
        print("Total price is :[%s]" % total_price)
    elif user_choice == "pay":
        total_price = 0
        print("You have bought below products.")

        for index, p in enumerate(shopping_car, 1):
            print(index, p)
            total_price += p[1]
        print("Total price is :[%s]" % total_price)
        pay_confirm = input("继续支付？[Y/N]").strip()
        if pay_confirm.upper() == "Y":
            money_left = int(user_asset) - total_price
            if money_left > 0:
                paid_list += shopping_car
                shopping_car = []
                user_asset = money_left
                print("Has paid [%s], current balance is [%s]" % (total_price,money_left))
                go_confirm = input("Press any key to continue shopping ...")
            else:
                print("You current balance is [%s], still need [%s]" % (user_asset,total_price-int(user_asset)))
    elif user_choice == "quit":
        if shopping_car:
            print("You still have some product haven't pay")
        else:
            print("Bye")
            break_flag = True