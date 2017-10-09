#!/usr/bin/env python
# -*- coding:utf-8 -*-
BeiJing_Map = {
    "通州区":{
        "潞城镇":{
            "潞城一村":{"a1":1},
            "潞城二村":{"a2":2},
            "潞城三村":{"a3":3},
        },
        "永顺镇":{
            "永顺一村":{"b1":4},
            "永顺二村":{"b2":5},
            "永顺三村":{"b3":6},
        },
        "梨园镇":{
            "梨园一村":{"c1":7},
            "梨园二村":{"c2":8},
            "梨园三村":{"c3":9},
        },
    },

    "大兴区":{
        "大兴1镇":{
            "大兴1镇一村":{"d1":11},
            "大兴1镇二村":{"d2":12},
            "大兴1镇三村":{"d3":13},
        },
        "大兴2镇":{
            "大兴2镇一村":{"e1":14},
            "大兴2镇二村":{"e2":15},
            "大兴2镇三村":{"e3":16},
        },
        "大兴3镇":{
            "大兴3镇一村":{"f1":17},
            "大兴3镇二村":{"f2":18},
            "大兴3镇三村":{"f3":19},
        },
    },
}
level=[]#定义空列表
while True:
    for key in BeiJing_Map:
        print(key)
    choice = input("【按b退出】请选择去哪》》》:")
    if choice == "b":#如果输入的是b
        if len(level) == 0:break#如果列表是空；就退出循环
        BeiJing_Map = level[-1]#输入b退到上一步时；BeiJing_Map等于列表的最后一个值
        level.pop()#删除列表的最后一个值
    #如果出入的是空；或者出入的不在BeiJing_Map中；退出；进行下次循环
    if len(choice) == 0 or choice not in BeiJing_Map:continue
    level.append(BeiJing_Map)#将输入的值；添加到level列表里
    #将输入的值赋给BeiJing_Map；在次循环
    BeiJing_Map = BeiJing_Map[choice]


















