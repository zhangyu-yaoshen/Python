#!/usr/bin/env python
# -*- coding:utf-8 -*-

product_list = [
    {"name": "电脑", "price": 8899},
    {"name": "鼠标", "price": 89},
    {"name": "键盘", "price": 99},
    {"name": "显示器", "price": 599},
    {"name": "苹果手机", "price": 999},
    {"name": "小米手机", "price": 1999},
    {"name": "华为手机", "price": 5999},
]
shopping_list = []#定义一个空列表；作为存放买到的商品
salary = input("你得余额：")
if salary.isdigit():#判断是一个数字,是整数返回true真
    salary = int(salary)#如果是数字给他int类型
    while True:#一个为真的循环
        for index,item in enumerate(product_list):#以标志位为序号循环列表
            #print(product_list.index(item),item)
            print(index,item)#打印以标志位为序号循环列表
        user_choice = input("请选择要买东西的序号：(退出请输入【q】)")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >=0:#判断输入的序号在0和列表长度之间
                p_item = product_list[user_choice]#给输入的序号为标志位的列表值加变量
                if p_item["price"] <= salary:#判断输入的余额是否大于商品的价格
                    shopping_list.append(p_item)#将标志位的列表值加入新表中；将买到的商品加入到新表中
                    salary -= p_item["price"]#余额减去商品的价格；标志位1所代表的数字
                    print("%s 加入购物车,你得余额是：\033[31;1m%s\033[0m" %(p_item,salary))
                else:
                    print("\033[41;1m你的余额只剩【%s】，什么都买不了。\033[0m" %salary)
            else:
                print("你输入的商品 【%s】 不存在" %user_choice)
        elif user_choice == "q":
            print("----------\033[32;1m你买到的商品\033[0m----------")
            for p in shopping_list:#循环买到的商品列表
                for k,v in p.items():
                    print(k,v)
                print("====================")
                #print(p)#打印商品列表
            print("你的余额是：\033[32;1m%s\033[0m" %salary)
            exit()#退出
        else:
            print("请输入数字")