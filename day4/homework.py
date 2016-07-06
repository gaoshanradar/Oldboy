#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng


def fetch(backend):
    #print("backend is : %s" % backend)
    #backend = “www.oldboy.org”
    result = []
    #打开配置文件
    with open('ha.conf', 'r', encoding='utf-8') as f:
        #设定跳出判断标记位
        flag = False
        #按行读取文件
        for line in f:
            #print("line is : %s"  % line)
            #匹配到backend行
            if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                #print("line is : %s"  % line)
                flag = True
                #匹配到backend后跳过这一行
                continue
            #flag = True时，配置文件中有两种情况：backend buy.oldboy.org和backend www.oldboy.org
            #读完backend这一行后继续后面读又出现了backend，即读到这一句：backend buy.oldboy.org
            if flag and line.strip().startswith("backend"):
                flag = False
                #终止
                break
            #匹配到backend且是一次匹配到backend，flag = True，backend www.oldboy.org,且去掉空字符串
            if flag and line.strip():
                #将"server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000"添加到结果列表中
                result.append(line.strip())

    return result

def add(backend, record):
    #先检查记录是否存在fetch()
    record_list = fetch(backend)
    #代码顺序，先易后难
    if not record_list:
        #backend不存在,需要新增backend和record,即把原文件全部写到新的文件中，然后在最后添加backend+record_list
        with open('ha.conf', 'r') as old, open('new.conf', 'w') as new:
            #读取一行旧的文件，写一行新的文件
            for line in old:
                new.write(line)
            #将新增的部分添加到新文件末尾
            #先加backend
            new.write("\nbackend " + backend + "\n")
            #后加server信息
            new.write(" " * 8 + record + "\n")
    else:
        #backend存在
        if record in record_list:
            #backend存在，record也存在
            import shutil
            #复制原文件
            shutil.copy("ha.conf", "new.conf")
        else:
            #backend存在，record不存在
            #不存在record则将其添加到内存列表中
            record_list.append(record)
            #将旧的文件读一行，在新的文件中写一行
            with open('ha.conf', 'r') as old, open('new.conf', 'w') as new:
                #如果读到backend，判断是否需要写到新的文件中
                flag = False
                for line in old:
                    #匹配到backend和输入的内容www.oldboy.org
                    if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                        #backend下面的内容不应写到文件中，标记True
                        flag = True
                        #接着将backend www.oldboy.org写到新文件中
                        new.write(line)
                        #回到内存中将record存放到record_list中的记录写到新的文件中，即"server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000"写到new中
                        for new_line in record_list:
                            new.write(" " * 8 + new_line + "\n")
                    #找到第二个backend，则读一行写一行
                    if flag and line.strip().startswith("backend"):
                        #判断需要将backend下面的内容写到文件中，标记False
                        flag = False
                        #将当前行写入新的文件中，即backend buy.oldboy.org写到新的文件中
                        new.write(line)
                        #加continue，防止下面读一行写一行时重复写backend buy.oldboy.org
                        continue
                    #若backend下面的行有数据，则读一行写一行
                    if not flag and line.strip():
                        new.write(line)

bk = "www.oldboy.org"
rd = "server 100.1.7.59 100.1.7.59 weight 60 maxconn 8000"
add(bk, rd)
#添加记录有三种情况：1、backend存在，记录也存在；2、backend不存在；3、backend存在但记录不存在


