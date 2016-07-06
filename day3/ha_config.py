#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng


import json

def check_conf(check_info):
    flag = False
    check_list = []
    with open('ha.conf') as f:
        for line in f:
            if line.startswith('backend'):
                if check_info == line.strip().split()[1]:
                    flag = True
                    continue
            if flag and line.strip().startswith('backend'):
                break
            if flag and line.strip():
                check_list.append(line.strip())
    return check_list

def add_conf(backend, record_conf):
    print("传入add函数后的值，backend is %s, record is : %s" % (backend, record_conf))
    #调用check_conf函数将查询到的server信息添加到列表中
    add_list = check_conf(backend)
    print("查询原文件中记录存入列表：%s" % add_list)
    #如果记录不存在，则将原文件内容写入新文件中，并在新文件末尾添加记录
    if not add_list:
        with open('ha.conf') as old, open('new_ha.conf', 'w') as new:
            for line in old:
                new.write(line)
            #在末尾直接添加记录,注意换行
            new.write("\nbackend " + backend + "\n")
            new.write(" "*8 + record_conf)
    else:
        #如果添加的记录存在
        if record_conf in add_list:
            print("记录已存在。")
        #原文件中有backend+server记录，但输入的记录需要更新到该记录下
        else:
            #将旧文件写入新文件标志位
            flag = False
            #写入add_list中存放的记录标志位
            write_flag = False
            #先输入的server记录存入列表中
            add_list.append(record_conf)
            #一边读旧文件一边写新的文件
            with open("ha.conf") as old, open("new_ha.conf", 'w') as new:
                for line in old:
                    #print("逐行打印文件：%s" % line)
                    #查找backend行
                    if line.startswith('backend'):
                        #print("打印backend开头的信息：%s" % line)
                        #遇到匹配的记录后，需要将backend所在行的记录写入新文件
                        if backend == line.strip().split()[1]:
                            new.write(line)
                            #打开写文件标志
                            flag = True
                            continue
                        #若再次匹配到backend说明到了下一个以backend开头的行，则反转写文件标志位
                    if line.startswith("backend"):
                        flag = False
                    #将两行backend之间的文件写入新文件中
                    if flag:
                        if not write_flag:
                            #循环add_list列表将记录写入新文件
                            for line_record in add_list:
                                new.write(" "*8 + line_record + "\n")
                                write_flag = True
                    else:
                        new.write(line)

def delete_conf(backend, record_conf):
    # print("backend : %s" % backend)
    # print("record : %s" % record_conf)
    # 调用check_conf函数将查询到的server信息添加到列表中
    del_list = check_conf(backend)
    # print(check_list)
    # 如果记录不存在，则将原文件内容写入新文件中，并在新文件末尾添加记录
    if not del_list:
        print("您输入的字段不存在。")
    else:
        # 如果添加的记录存在
        if record_conf in del_list:
            del_list.remove(record_conf)
            # 将旧文件写入新文件标志位
            flag = False
            # 写入check_list中存放的记录标志位
            write_flag = False
            # 一边读旧文件一边写新的文件
            with open("ha.conf") as old, open("new_ha.conf", 'w') as new:
                for line in old:
                    # 查找backend行
                    if line.startswith('backend'):
                        # 遇到匹配的记录后，需要将backend所在行的记录写入新文件
                        if backend == line.strip().split()[1]:
                            new.write(line)
                            # 打开写文件标志
                            flag = True
                            continue
                    # 若再次匹配到backend说明到了下一个以backend开头的行，则反转写文件标志位
                    if line.startswith("backend"):
                        flag = False
                    # 将两行backend之间的文件写入新文件中
                    if flag:
                        if not write_flag:
                            # 循环check_list列表将记录写入新文件
                            for line_record in del_list:
                                new.write(" " * 8 + line_record + "\n")
                                write_flag = True
                    else:
                        new.write(line)
        else:
            print("您输入的记录不存在。")

def menu():
    print(
    """
    **********操作编号***********
    1 查看
    2 增加
    3 删除
    *****************************
    """
)

def json_conf(record,input_conf):
    print("json is : %s %s" % (record, input_conf))
    dict_conf = json.loads(record)
    backend = dict_conf['backend']

    record_conf = "server %s %s weight %d maxconn %d" % (dict_conf['record']['server1'],
                                                         dict_conf['record']['server2'],
                                                         dict_conf['record']['weight'],
                                                         dict_conf['record']['maxconn'])

    print("处理完成后,backend is : %s ,record is : %s" % (backend, record_conf))
    if input_conf == '2':
        add_conf(backend, record_conf)
    if input_conf == '3':
        delete_conf(backend, record_conf)

def main():
    menu()
    flag = False
    while not flag:
        input_conf = input("请输入操作编号：")
        if input_conf == '1':
            check_info = input("请按照以下格式输入：(www.oldboy.org) ")
            if check_conf(check_info):
                flag = True
                for k,v in enumerate(check_conf(check_info),1):
                    print(k,':',v)
            else:
                print("您输入的字段不存在。")
                flag = False
        elif input_conf == '2':
            add_info = input('''请按照以下格式添加数据：
            {"backend":"www.oldboy.org","record":{"server1":"100.1.27.9","server2":"100.1.37.19","weight":20, "maxconn":3000}}
            ''')
            json_conf(add_info, input_conf)
            flag = True
        elif input_conf == '3':
            del_info = input('''请按照以下格式添加数据：
                {"backend":"www.oldboy.org","record":{"server1":"100.1.7.9","server2":"100.1.7.19","weight":20, "maxconn":3000}}
                ''')
            json_conf(del_info, input_conf)
            flag = True
        else:
            print("你输入的操作编号不存在，请重新输入")
            flag = False


if __name__ == '__main__':
    main()