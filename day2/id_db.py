#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng

id_db = {
    421087198901298697: {
        'name': 'radar',
        'age' : 22,
        'addr':'HuBei',
    },
    421087154671298697: {
        'name': 'snow',
        'age': 22,
        'addr': 'AnHui',
    },
    421087133221298697: {
        'name': 'fish',
        'age': 10,
        'addr': 'Shanxi',
    },
}
#自动去重，key需唯一
print(id_db)
print(id_db[421087133221298697])
#修改
id_db[421087133221298697]['name'] = "NiuRen"
print(id_db[421087133221298697])
#删除
id_db.pop(421087133221298697)
print(id_db)
id_db[421087154671298697].pop("addr")
print(id_db)
#copy复制
#clear清空
#get获取
v = id_db.get(421087198901298697)
print(v)
#update
dict1 = {
    'name':'Bottle',
    421087154671298697: {
        'name': 'radar',
    },
}
id_db.update(dict1)
print(id_db)

print(id_db)
#id_db.items()把字典转换为元组，数据量大时不要使用
print(id_db.items())

dict_values = id_db.values()
dict_keys = id_db.keys()
print(dict_keys)
print(dict_values)
421087154671298697 in id_db #eauals to above has key(x)

id_db.setdefault(421087154671298697,"haha") #取一个值key，如果不存在就设置一个值；如果存在直接设置值
print(id_db)

print(dict.fromkeys([1,2,3,4,5]),'bfgb')   #把字典里的所有值都当作key

print(id_db.popitem())  #随机删除，尽量不要用

for k,v in id_db.items():   #效率低，需要有一个字典转换为列表操作
    print(k)
    print(v)
for key in id_db:   #效率高
    print(key,id_db[key])


