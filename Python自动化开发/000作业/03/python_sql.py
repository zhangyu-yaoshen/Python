#!/usr/bin/env python
# -*- coding:utf-8 -*-
#第一部分：sql解析
def sql_parse(sql):
    """sql解析；把sql字符串切分；提取命令信息；分发给具体的函数解析
    四种操作方法insert delete update select
    将四个功能分发给四个函数
    select * from db1.员工信息表 where id>3 limit 3
    """
    parse_func={
        "insert":insert_parse,
        "delete":delete_parse,
        "update":update_parse,
        "select":select_parse,
    }#不能加括号；加括号是函数的执行结果；不加是执行函数
    print("sql语句是》》%s" %sql)#打印的字符串是已空格分割的
    sql_l=sql.split(" ")#已空格分割字符串
    func=sql_l[0]#筛选字符串第一个值
    res=""
    if func in parse_func:#判断如果第一个字符在字典里
        res=parse_func[func](sql_l)#调用函数并传递参数（sql_l）
    return res

def insert_parse(sql_l):
    """
    增
    定义insert语句的语法结构；执行sql解析操作；返回sql_dic
    """
    pass
def delete_parse(sql_l):
    """
    删
    定义delete语句的语法结构；执行sql解析操作；返回sql_dic
    :param sql:
    :return:
    """
    pass
def update_parse(sql_l):
    """
    改
    定义update语句的语法结构；执行sql解析操作；返回sql_dic
    :param sql:
    :return:
    """
    pass
def select_parse(sql_l):
    """
    查
    定义select语句的语法结构，执行sql解析操作，返回sql_dic
    :param sql_l:
    :return:
    """

    print('from in the select_parse \033[32;1m%s\033[0m'% sql_l)
    #定义语法结构
    sql_dic={
        "func":select,
        "select":[],    #查询字段
        "from":[],      #数据表
        "where":[],     #filter条件【过滤条件】
        "limit":[],     #limit条件【限制条件】
    }
    #返回值；调用handle_parse函数
    return handle_parse(sql_l,sql_dic)#将sql_L参数和自己定义的sql_dic传给handle——parse



def handle_parse(sql_l,sql_dic):
    """
    执行sql解析操作；返回sql_dic
    :param sql_l:
    :param sql_dic:
    :return:
    """
    print("sql_l is %s; /n sql_dic is %s" %(sql_l,sql_dic))

    pass






#第二部分：sql执行
def sql_action(sql_dic):
    """
    从字典sql_dic提取命令；分发给具体的命令执行函数去执行
    """
    pass
def insert_action(sql_dic):
    """
    增
    """
    pass
def delete_action(sql_dic):
    """
    删
    :param sql:
    :return:
    """
    pass
def update_action(sql_dic):
    """
    改
    :param sql:
    :return:
    """
    pass
def select_action(sql_dic):
    """
    查
    :param sql:
    :return:
    """
    pass







if __name__ == "__main__":#当直接执行本文件时；执行下面的语句；
    while True:#真循环；无限循环
        sql = input("sql> ").strip()#输入sql语句；去除两边空格
        if sql == "exit":break#如果输入exit就退出
        if len(sql) == 0:continue#如果输入空就重新循环

        sql_dic=sql_parse(sql)#调用sql解析函数；并得到返回值
        res=sql_action(sql_dic)#执行完sql的返回结果







