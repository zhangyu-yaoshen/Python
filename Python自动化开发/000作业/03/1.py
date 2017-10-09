#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
#第一部分 sql解析
def sql_parse(sql):
    parse_func={
        'insert':insert_parse,
        'delete':delete_parse,
        'update':update_parse,
        'select':select_parse,
    }
    # print('sql str is %s '%sql)
    sql_l=sql.split(' ') #list
    func=sql_l[0]
    res=''
    if func in parse_func:
        res=parse_func[func](sql_l)
    return res
def insert_parse(sql_l):
    sql_dic = {
        'func': insert,
        'insert': [],
        'into': [],  # data.emp
        'values': [],
    }
    return handle_parse(sql_l,sql_dic)
def delete_parse(sql_l):
    sql_dic = {
        'func': delete,
        'delete': [],  # search
        'from': [],  # data.emp
        'where': [],  # filter condition
    }
    return handle_parse(sql_l, sql_dic)
def update_parse(sql_l):
    sql_dic = {
        'func': update ,
        'update': [],  # search
        'from': [],
        'where': [],
        'set': [],  # filter condition
    }
    return handle_parse(sql_l, sql_dic)
def select_parse(sql_l):
    # print('from in the select_parse \033[32;1m%s\033[0m'%sql_l)
    sql_dic={
        'func':select,
        'select':[] ,#search
        'from':[], #data.emp
        'where':[], #filter condition
        'limit':[], #limit condition
    }
    return handle_parse(sql_l,sql_dic)
def  handle_parse(sql_l,sql_dic):
    """
    执行sql解析操作，返回sql_dic
    :param sql_l:
    :param sql_dic:
    :return:
    """
    # print('sql_l is \033[32;1m%s\033[0m \nsql_dic is \033[41;1m%s\033[0m'%(sql_l,sql_dic))
    tag=False
    for item in sql_l:
        if tag and item in sql_dic:
            tag=False
        if not tag and item in sql_dic:
            tag=True
            key=item
            continue
        if tag:
            sql_dic[key].append(item)
    if sql_dic.get('where'):
        sql_dic['where']=where_parse(sql_dic.get('where')) #['id>4,'and','id<10']

    # print('from in the handle_parse sql_dic is \033[32;1m%s\033[0m'%sql_dic)
    return sql_dic
#整合字符串
def where_parse(where_l):#['not','id>','4',' ','and','id','<10']
    res=[]
    key=['and','or','not']
    char=''
    for i in where_l:
        if len(i)==0:continue
        if i in key:
             # i为key当中存放的逻辑运算符
             if len(char)!=0:
                char=three_parse(char)
                res.append(char)  #char='id>4'-->char=['id','>','4']
                res.append(i)
                char=''
        else:
            char+=i #'id<10'
    else:
        char = three_parse(char)
        res.append(char)
        # print('from in the where_parse res is \033[32;1m%s\033[0m' % res)
    return res
def three_parse(exp_str):
    """
    'id<=10'-->["id",'<=","10"]
    :param exp_str:
    :return:
    """
    key=[">","<","="]
    res=[]
    char=''
    opt=''
    tag=False
    for i in exp_str:
        if i in key:
            tag=True
            if len(char)!=0:

                res.append(char) #append id,digit
                char=''
            opt+=i  #opt='<='
        if not tag:
            char+=i  #char='id'
        #appened <,>,=
        if tag and i not in key:
            tag=False
            res.append(opt)
            opt=' '
            char+=i #char='1'

    else:
        res.append(char)
    #新增解析like功能
    # print('------%s'%res)
    if len(res) == 1:
        res=res[0].split('like')
        res.insert(1,'like')
    # print('three_parse res is \033[41;1m%s\033[0m'%res)
    return res

#第二部分 sql执行
def sql_action(sql_dic):
    """
    从字典sql_dic提取命令，分发给具体的命令执行函数去执行
    :param sql_dic:
    :return:
    """
    return  sql_dic.get('func')(sql_dic)   #sql_dic.get('func')==select
def insert(sql_dic):
    # print('insert %s'%sql_dic)
    db, table = sql_dic.get('into')[0].split('.')
    with open("%s/%s" % (db, table), 'ab+') as fh:
        #读取文件最后一行
        offs = -100
        while True:
            fh.seek(offs, 2)
            lines = fh.readlines()
            if len(lines) > 1:
                last = lines[-1]
                break
            offs *= 2
        last = last.decode(encoding='utf-8')
        #id++
        last_id = int(last.split(',')[0])
        new_id = last_id + 1
        #insert into dbl.emp values 张国辉,30,18234561234,运维,2007-8-1
        record = sql_dic.get('values')[0].split(',')
        record.insert(0, str(new_id))
        record_str = ','.join(record) + '\n'#list-->str
        fh.write(bytes(record_str, encoding='utf-8'))
        fh.flush()
    return [['insert successful']]
def delete(sql_dic):
    # print('--->%s'%sql_dic.get('from'))
    db, table = sql_dic.get('from')[0].split('.')
    bak_file = table + 'bak'
    with open("%s/%s" % (db, table), 'r', encoding='utf-8')as r_file, \
            open("%s/%s" % (db, bak_file), "w", encoding='utf-8')as w_file:
        del_count = 0
        for line in r_file:
            title = "id,name,age,phone,dept,enroll_data"
            dic = dict(zip(title.split(','), line.split(',')))
            filter_res = logic_action(dic, sql_dic.get('where'))
            if not filter_res:
                w_file.write(line)
            else:
                del_count += 1
        w_file.flush()
    os.remove("%s/%s" % (db, table))
    os.rename("%s/%s" % (db, bak_file), "%s/%s" % (db, table))
    return [[del_count], ['delete successful']]
def update(sql_dic):
    # update dbl.emp set name='sb' where id=1
    db, table = sql_dic.get('update')[0].split('.')
    set = sql_dic.get('set')[0].split(',')
    set_l = []
    for i in set:
        set_l.append(i.split('='))
    bak_file = table + 'bak'
    with open("%s/%s" % (db, table), 'r', encoding='utf-8')as r_file, \
            open("%s/%s" % (db, bak_file), 'w', encoding="utf-8") as w_file:
        update_count = 0
        for line in r_file:
            title = "id,name,age,phone,dept,enroll_data"
            # print(line)
            dic = dict(zip(title.split(','), line.split(',')))
            # print('----%s'%dic)
            filter_res = logic_action(dic, sql_dic.get('where'))
            if filter_res:
                # print(set_l)
                for i in set_l:
                    k = i[0] #name
                    v = i[-1].strip(",") #alex
                    # print("k:%sv:%s" % (k,v))
                    dic[k] = v
                # print('change dic is %s' % dic)
                line = []
                for i in title.split(','):
                    line.append(dic[i])
                update_count += 1
                line = ','.join(line)
            w_file.write(line)
            # print('>>>>%s'%line)
        w_file.flush()
    os.remove("%s/%s" % (db, table))
    os.rename("%s/%s" % (db, bak_file), "%s/%s" % (db, table))
    return [[update_count], ['update successful']]
def select(sql_dic):
    print('from select sql_dic is %s'%sql_dic)
    db,table=sql_dic.get('from')[0].split('.')
    fh=open('%s/%s'%(db,table),'r',encoding='utf-8')
    filter_res=where_action(fh,sql_dic.get('where')) #筛选where
    # for record in filter_res:
    #     print('filter res is %s'%record)
    limit_res=limit_action(filter_res,sql_dic.get('limit'))#筛选where+limit
    # for record in limit_res:
    #     print('limit res is %s'%record)
    search_res=search_action(limit_res,sql_dic.get('select'))#筛选where+limit+select
    # for record in search_res:
    #     print('search res is %s'%record)
    return search_res
def limit_action(filter_res,limit_l):
    res=[]
    if len(limit_l) !=0:
        index=int(limit_l[0])
        res=filter_res[0:index]#index=='3',列表切片
    else:
        res=filter_res
    return res
def search_action(limit_res,select_l):#select_l ['id,name']
    # print('search_action limit res:%s'%limit_res)
    res=[]
    fields_l=[]
    title="id,name,age,phone,dept,enroll_data"
    if select_l[0] == '*':
        fields_l=title.split(',')
        res=limit_res
    else:
        for record in limit_res:
            dic=dict(zip(title.split(','),record))#生成字典
            r_l=[]
            fileds_l=select_l[0].split(',')#'id','name'
            for i in fileds_l:
                r_l.append(dic[i].strip())
            res.append(r_l)
    # print('search_action r_l %s,%s'%(fields_l,r_l))
    return(fields_l,res)
def where_action(fh,where_l):
    """

    :return:
    """
    # print('\033[41;1m%s\033[0m'%where_l)
    res=[]
    logic_l=['and','or','not']
    title="id,name,age,phone,dept,enroll_data"
    if len(where_l) != 0:
        for line in fh:
            dic=dict(zip(title.split(','),line.split(','))) #生成字典的格式，一条记录
            #逻辑判断
            logic_res=logic_action(dic,where_l)
            if logic_res:
                res.append(line.split(','))
    else:
        fh.readlines()
    return res
def logic_action(dic,where_l):
    # print('from logic_action%s'%dic)
    # print(where_l)
    res=[]
    for exp in where_l:
        #dic与exp做布尔运算
        if type(exp) is list:
            #做布尔运算
            exp_k,opt,exp_v=exp
            if exp[1]=='=':
                opt="%s="%exp[1]
            if dic[exp_k].isdigit(): #是否是数字
                dic_v=int(dic[exp_k])
                exp_v=int(exp_v)
            else:
                dic_v="'%s'"%dic[exp_k].strip()
            if opt !='like':
                # print('--->%s\n%s\n%s'%(dic_v,opt,exp_v))
                exp=str(eval("%s%s%s"%(dic_v,opt,exp_v)))
            else:
                if exp_v in dic_v:
                    exp="True"
                else:
                    exp="False"
        res.append(exp) #['True','or','False','or','True']
    res=eval(' '.join(res)) #布尔运算
    return res

#主程序
if __name__ == '__main__':
    while True:
        sql=input('sql>:').strip()
        if sql=='exit':break
        if len(sql) == 0: continue


        sql_dic=sql_parse(sql)
        if not sql_dic:
            print('输入非法，请重新输入！')
            continue
        res=sql_action(sql_dic)
        count = 0
        for record in res[-1]:
            tag=True
            if 'select' in sql_dic and tag:
                print('符合条件的记录:%s'%record)
                count+=1
            else:
                tag=False
                print(record)
        if tag:
            print('一共查到记录%s条。' % count)