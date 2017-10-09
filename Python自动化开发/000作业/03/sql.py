#!/usr/bin/env python
# -*- coding:utf-8 -*-
def sql_parse(sql):
    parse_func={
        'select':select_parse,
    }
    # print('sql str is %s '%sql)
    sql_l=sql.split(' ') #list
    func=sql_l[0]
    res=''
    if func in parse_func:
        res=parse_func[func](sql_l)
    return res


def select_parse(sql_l):
    print('from in the select_parse \033[32;1m%s\033[0m'%sql_l)





if __name__ == "__main__":#当直接执行本文件时；执行下面的语句；
    while True:#真循环；无限循环
        sql = input("sql> ").strip()#输入sql语句；去除两边空格
        if sql == "exit":break#如果输入exit就退出
        if len(sql) == 0:continue#如果输入空就重新循环

        sql_dic=sql_parse(sql)#调用sql解析函数；并得到返回值
        #res=sql_action(sql_dic)#执行完sql的返回结果





