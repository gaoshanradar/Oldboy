#！/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: wanghuafeng

age = 22
counter = 0
for i in range(10):
    print("counter is :", counter)
    if counter < 3:
        guess_num = int(input("input your guess num:  "))
        if guess_num == age:
            print("Congratulations! You got it.")
            break
        elif guess_num > age:
            print("Think smaller!")
        else:
            print("Think Big...")
    else:
        continue_confirm = input("Do you want to continue because you are stupid:")
        if continue_confirm == 'y':
            counter = 0
            continue
        else:
            print("Bye.")
            break
    counter += 1