#!/usr/bin/env python
# -*- coding:utf-8 -*-
#第一部分：sql解析
def sql_parse(sql):
    """sql解析；把sql字符串切分；提取命令信息；分发给具体的函数解析
    四种操作方法insert delete update select
    将四个功能分发给四个函数
    select * from db1.emp where id> 3 and id <5 limit 3
    """
    parse_func={
        "insert":insert_parse,
        "delete":delete_parse,
        "update":update_parse,
        "select":select_parse,
    }#不能加括号；加括号是函数的执行结果；不加是执行函数
    #print("sql语句是》》%s" %sql)#打印的字符串是已空格分割的
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

    #print('from in the select_parse \033[32;1m%s\033[0m'% sql_l)
    #定义语法结构
    sql_dic={
        "func":select,  #调用执行语句用
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
    #打印sql_l和sql_dic看看效果
    #print("sql_l is %s;\nsql_dic is %s" %(sql_l,sql_dic))
    tag=False#制作标准位
    for item in sql_l:#循环sql_l
        if tag and item in sql_dic:##如果标志位真的；并且item在sql_dic里
            tag=False#将标志位改为假
        if not tag and item in sql_dic:#如果标志位不是假的；并且item在sql_dic里
            tag=True#将标志位改为真
            key=item#给item赋值
            continue#退出；开始下次循环
        if tag:#如果标志位位真
            sql_dic[key].append(item)#将值添加到sql_dic[key]里
    if sql_dic.get("where"):#处理where语句
        sql_dic["where"]=where_parse(sql_dic.get("where"))#建立新的函数处理where
    #print("拼接好的sql字典",sql_dic)
    return sql_dic

def where_parse(where_l):
    """
    处理where语句
    由['id>', '3', 'and', 'id', '<5']转换成['id>3', 'and', 'id<5']
    :param where_l:
    :return:
    """
    #print("这是where语句",where_l)
    res=[]#存放处理好的数据
    key=["and","or","not"]
    char=""
    for i in where_l:#循环where_l
        if len(i) == 0:continue#如果遇到空格就进行下次循环
        if i in key:#如果i在key里
            if len(char) != 0:#如果char不等于0
                char= three_parse(char)#处理char成['id','>','3']
                res.append(char)#res添加char
                res.append(i)#res添加i
                char=""#滞空char；一边下一个写入
        else:
            char+=i#拼接key前边的值
    else:
        res.append(char)#拼接key后面的值
    #['id>3', 'and', 'id<5', 'or', 'namelike李']转换成[['id','>','3'], 'and', ['id','<','5']', 'or', 'namelike李']
    #print(res)#['id>3', 'and', 'id<5']
    return res

def three_parse(exp_str):
    """
    #['id>3', 'and', 'id<5', 'or', 'namelike李']转换成[['id','>','3'], 'and', ['id','<','5']', 'or', 'namelike李']
    :param exp_str:
    :return:
    """
    key=[">","<","="]
    red=[]
    char=""#字符串
    opt=""#运算符
    tag=False
    for i in exp_str:#循环接收的字符串
        if i in key:#如果i是运算符
            tag=True#
        if not tag:#当tag不是真
            char+=i#将值添加到char








#第二部分：sql执行
def sql_action(sql_dic):
    """
    从字典sql_dic提取命令；分发给具体的命令执行函数去执行
    """
    sql_dic.get("func")(sql_dic)#根据func分发

def insert(sql_dic):
    """
    增
    """
    pass
def delete(sql_dic):
    """
    删
    :param sql:
    :return:
    """
    pass
def update(sql_dic):
    """
    改
    :param sql:
    :return:
    """
    pass
def select(sql_dic):
    """
    查操作
    优先级
    1、from
    2、where
    3、limit
    4、select
    """
    print("这里是查操作执行 \033[32;1m%s\033[0m"%sql_dic)
    #处理from
    db, table =sql_dic.get("from")[0].split(".")#确定库名表名【多元素值；将值赋给前面的变量】
    fh=open("%s/%s" %(db,table),"r",encoding="utf-8")#打开文件
    #处理where【select * from db1.a.txt where id> 3 and id <5 or name like 李】
    filter_res=where_action(fh,sql_dic.get("where"))#将打开的文件；和自动的where信息传给where_action函数

def where_action(fh,where_l):
    """
    传入参数为fh和sql_dic.get("where")
    ['id>3', 'and', 'id<5', 'or', 'namelike李']
    :param fh:
    :param where_l:
    :return:
    """
    pass






if __name__ == "__main__":#当直接执行本文件时；执行下面的语句；
    while True:#真循环；无限循环
        sql = input("sql> ").strip()#输入sql语句；去除两边空格
        if sql == "exit":break#如果输入exit就退出
        if len(sql) == 0:continue#如果输入空就重新循环

        sql_dic=sql_parse(sql)#调用sql解析函数；并得到返回值
        #print("这是组建的sql的语句",sql_dic)
        if len(sql_dic) == 0:continue#如果返回空；就退出本次循环；开始下次循环
        res=sql_action(sql_dic)#执行完sql的返回结果







