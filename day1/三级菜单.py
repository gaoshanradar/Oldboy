#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author: WangHuafeng


# 一级菜单： 商品分类
def show_category ():
    category_list = (
        {'cid': '1', 'cname': '手机类'},
        {'cid': '2', 'cname': '服装类'},
        {'cid': '3', 'cname': '家电类'},
        {'cid': '4', 'cname': '食品类'},
        {'cid': '5', 'cname': '特产类'},
    )
    return category_list

# 二级菜单： 各类商品中的品牌
def show_brand():
    brand_list = (
        ({'bid': '1-1', 'bname': '小米'},
         {'bid': '1-2', 'bname': '三星'},
         {'bid': '1-3', 'bname': '苹果'},),
        ({'bid': '2-1', 'bname': '劲霸'},
         {'bid': '2-2', 'bname': '利郎'},
         {'bid': '2-3', 'bname': '七匹狼'},),
        ({'bid': '3-1', 'bname': '海尔'},
         {'bid': '3-2', 'bname': '美的'},
         {'bid': '3-3', 'bname': '格力'},),
        ({'bid': '4-1', 'bname': '热干面'},
         {'bid': '4-2', 'bname': '藕带'},
         {'bid': '4-3', 'bname': '鱼糕'},),
    )
    return brand_list


# 三级菜单： 价钱
def show_area():
    area_list = (
        ({'aid': '1-1-1', 'aname': '阜成门'},{'aid': '1-1-2', 'aname': '长椿街'},{'aid': '1-1-31', 'aname': '宣武门'},),
        ({'aid': '1-2-1', 'aname': '金宝街'},{'aid': '1-2-2', 'aname': '珠市口'},{'aid': '1-2-3', 'aname': '东直门'},),
        ({'aid': '1-3-1', 'aname': '中关村'},{'aid': '1-3-2', 'aname': '西二旗'},{'aid': '1-3-3', 'aname': '肖家河'},),
        ({'aid': '2-1-1', 'aname': '长安区'}, {'aid': '2-1-2', 'aname': '桥东区'}, {'aid': '2-1-3', 'aname': '桥西区'},),
        ({'aid': '2-2-1', 'aname': '新市区'}, {'aid': '2-2-2', 'aname': '北市区'}, {'aid': '2-2-3', 'aname': '南市区'},),
        ({'aid': '2-3-1', 'aname': '邢台县'}, {'aid': '2-3-2', 'aname': '内丘县'}, {'aid': '2-3-3', 'aname': '柏乡县'},),
        ({'aid': '3-1-1', 'aname': '金水区'}, {'aid': '3-1-2', 'aname': '二七区'}, {'aid': '3-1-3', 'aname': '上街区'},),
        ({'aid': '3-2-1', 'aname': '龙亭区'}, {'aid': '3-2-2', 'aname': '南关区'}, {'aid': '3-2-3', 'aname': '开封县'},),
        ({'aid': '3-3-1', 'aname': '老城区'}, {'aid': '3-3-2', 'aname': '西工区'}, {'aid': '3-3-3', 'aname': '新安县'},),
        ({'aid': '4-1-1', 'aname': '江岸区'}, {'aid': '4-1-2', 'aname': '江汉区'}, {'aid': '4-1-3', 'aname': '武昌区'},),
        ({'aid': '4-2-1', 'aname': '宜昌县'}, {'aid': '4-2-2', 'aname': '远安县'}, {'aid': '4-2-3', 'aname': '新山县'},),
        ({'aid': '4-3-1', 'aname': '东宝区'}, {'aid': '4-3-2', 'aname': '京山县'}, {'aid': '4-3-3', 'aname': '沙洋县'},),

    )
    return area_list


