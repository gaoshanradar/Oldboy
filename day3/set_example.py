#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: WangHuafeng
#set:无序，不重复，可嵌套


old_dict = {
    "#1": 8,
    "#2": 4,
    "#4": 2,
}

new_dict = {
    "#1": 4,
    "#2": 4,
    "#3": 2,
}
#应该删除哪几个槽位
old_set = set(old_dict.keys())
new_set = set(new_dict.keys())
old_set.difference()
#需要删除的，old中有new中没有
remove_set = old_set.difference(new_set)
print("需要删除的槽位:%s" % remove_set)
#需要增加的，new中有old没有
add_set = new_set.difference(old_set)
print("需要增加的槽位:%s" % add_set)
#需要更新的，old和new的交集
update_set = old_set.intersection(new_set)
print("需要更新的槽位:%s" % update_set)