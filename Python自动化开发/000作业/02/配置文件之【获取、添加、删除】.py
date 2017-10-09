#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
frontend oldboy.org
        bind 0.0.0.0:80
        option httplog
        option httpclose
        option  forwardfor
        log global
        acl www hdr_reg(host) -i www.oldboy.org
        use_backend www.oldboy.org if www


backend www.oldboy.org
        server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000
        server 100.2.8.9 100.2.8.9 weight 80 maxconn 9000
backend buy.oldboy.org
        server 100.11.17.19 100.11.17.19 weight 20 maxconn 3000
backend smy.oldboy.org
        server 100.31.37.39 100.31.37.39 weight 20 maxconn 3000
#功能：获取、添加、删除
#打开文件，找到代码块，拿出来
"""
import json,os

"""
获取模块

"""
def fetch(backend):
    fetch_list = []#建立个空表存放要找的数据
    with open("ha.txt") as obj:#打开文件
        flag = False#定义标准位；用于判断是否是需要的backend
        for line in obj:#打开这个文件,循环执行每一行
            # 如果去除空格后，第一段单词是backend，并且后面是backend所代表的函数
            if line.strip() == "backend %s" % backend:
                flag = True
                continue#结束本次循环
            #判断，如果flag等于true时,并且遇到下个当前行是backend开头，不在放
            if flag and line.strip().startswith("backend"):
                flag = False
            if flag and line.strip():#当flag等于true时，并且是空行是，在fetch_list里添加数据
                fetch_list.append(line.strip())
        #for p in fetch_list:#循环fetch_list表中的数据
            #print(p)#打印数据
    return fetch_list

"""
添加模块
arg = {
    'bakend': 'buy.oldboy.org',
    'record':{
        'server': '999.99.99.99',
        'weight': 99,
        'maxconn': 9999
    }
思路：
1、获取backend；判断backend是否存在；
        存在：查看已知的数据是否在backend中；没有就添加到fetch_list中的；有退出
        不存在：建立backend；行写入数据
2、有的话；思路和添加一样；原配置文件里读一行；在新配置文件里写一行；
3、当写到backend的时候；写入新的fetch_list（里面没有删除的数据）
4、设定2个标志：flag和has_write
            #flag:用于找到要添加的backend下的内容
            #has_write:用于判断fetch_list中的内容是否重新写入到了文件
"""
#添加模块
def add1(app_info):
    add1_backend = app_info.get('backend')#取出backend后面的abc.oldboy.org
    current_title = "backend %s" %add1_backend#构造出backend abc.oldboy.org数据
    #构造字符串“server 100.11.17.19 100.11.17.19 weight 20 maxconn 3000”
    current_record = "server %s %s weight %d maxconn %d" % (app_info['record']['server'],app_info['record']['server'],app_info['record']['weight'],app_info['record']['maxconn'])
    fetch_list = fetch(add1_backend)#通过获取函数取出delete_backend的值
    #print(fetch_list)
    if fetch_list:#判断函数；有数据为真；没数据为假
        if current_record in fetch_list:#如果current_record所代表的数据；在fetch_list里
            pass#空操作什么都不做
        else:
            fetch_list.append(current_record)#将current_record所代表的数据添加到fetch_list里
        with open("ha.txt", "r") as read_obj, open("ha.new", "w") as write_obj:#打开原文件和新文件
            flag = False#定义标志位；用于确定current_title
            has_write = False#定义标志位；用于确定是否已经将current_title下面的字符串写入新表
            for line in read_obj:#循环读取原配置文件每一行
                if line.strip() == current_title:#如果遇到current_title；
                    write_obj.write(line)#把current_title所在行写入新配置文件
                    flag = True#标志位：为真；用来标记已经在current_title下
                    continue#结束单次循环
                if flag and line.startswith("backend"):#如果标志位为真；并且；下一行开头是【backend】
                    flag = False#定义标志位；已经离开current_title
                if flag:#如果标志位为真
                    if not has_write:#如果标志位为真；不为假；即为真
                        for new_line in fetch_list:#定义循环；循环fetch_list中剩余的字符串
                            temp = "%s%s\n" % (" " * 8, new_line)# 给字符串前加上8个空格
                            write_obj.write(temp)#将处理好的字符串写入新的配置文件
                        has_write = True#定义标志位为真；fetch_list中的内容是否重新写入到了文件
                else:
                    write_obj.write(line)#将原配置文件写入新配置文件

    else:
        with open("ha.txt", "r") as read_obj, open("ha.new", "w") as write_obj:#打开原文件和新文件
            flag = True#定义标志位为真；给while用
            for line in read_obj:#循环读取原配置文件每一行
                if line.strip() == current_title:#如果遇到current_title；
                    write_obj.write(line)  # 把current_title所在行写入新配置文件
                    temp = "%s%s\n" % (" " * 8, current_record)  # 给字符串前加上8个空格
                    write_obj.write(temp)  # 将处理好的字符串写入新的配置文
                    flag = False#标志位为假；while不循环
                else:
                    write_obj.write(line)  # 将原配置文件写入新配置文件
            while flag:#标志位为真；while循环；为假；while不循环
                write_obj.write("\n" + current_title + "\n")# 把构造好的backend写入新配置文件；并加入换行符
                temp = "%s %s\n" % (" " * 8, current_record)# 给数据前加上8个空格
                write_obj.write(temp)#将处理好的字符串写入新的配置文件
                flag = False#标志位为假；while不循环


    # else:
    #     with open("ha.txt", "r") as read_obj, open("ha.new", "w") as write_obj:#打开原文件和新文件
            #print(fetch_list)
            # for line in read_obj:#循环读取原配置文件每一行
            #     write_obj.write(line)#将原配置文件写入新配置文件
            # write_obj.write("\n" + current_title + "\n")# 把构造好的backend写入新配置文件；并加入换行符
            # temp = "%s %s\n" % (" " * 8, current_record)# 给数据前加上8个空格
            # write_obj.write(temp)#将处理好的字符串写入新的配置文件
    os.rename("ha.txt","ha.txt.bak")#将原配置文件备份
    os.rename("ha.new","ha.txt")#将新配置文件更名为原配置文件名


app_speiido = '{"backend": "AAA.oldboy.org","record":{"server": "100.9.0.9","weight": 20,"maxconn": 3990}}'
app_dict = json.loads(app_speiido)#将json编码的字符串再转换为python的数据结构
#add1(app_dict)
"""
#删除模块
1、获取backend；查看已知的数据是否在backend中；有则删除fetch_list中相应的数据；没有退出
2、有的话；思路和添加一样；原配置文件里读一行；在新配置文件里写一行；
3、当写到backend的时候；写入新的fetch_list（里面没有删除的数据）
4、设定2个标志：flag和has_write
            #flag:用于找到要添加的backend下的内容
            #has_write:用于判断fetch_list中的内容是否重新写入到了文件
"""
def delete(del_info):
    delete_backend = del_info.get('backend')#取出backend后面的abc.oldboy.org
    current_title = "backend %s" %delete_backend#构造出backend abc.oldboy.org数据
    #构造字符串“server 100.11.17.19 100.11.17.19 weight 20 maxconn 3000”
    current_record = "server %s %s weight %d maxconn %d" % (del_info['record']['server'],del_info['record']['server'],del_info['record']['weight'],del_info['record']['maxconn'])
    fetch_list = fetch(delete_backend)#通过获取函数取出delete_backend的值
    if fetch_list:#判断函数；有数据为真；没数据为假
        if current_record in fetch_list:#如果current_record所代表的数据；在fetch_list里
            fetch_list.remove(current_record)#删除fetch_list里的current_record所代表的数据
        else:
            return
        with open("ha.txt", "r") as read_obj, open("ha.new", "w") as write_obj:#打开原文件和新文件
            flag = False#定义标志位；用于确定current_title
            has_write = False#定义标志位；用于确定是否已经将current_title下面的字符串写入新表
            for line in read_obj:#循环读取原配置文件每一行
                if line.strip() == current_title:#如果遇到current_title；
                    write_obj.write(line)#把current_title所在行写入新配置文件
                    flag = True#标志位：为真；用来标记已经在current_title下
                    continue#结束单次循环
                if flag and line.startswith("backend"):#如果标志位为真；并且；下一行开头是【backend】
                    flag = False#定义标志位；已经离开current_title
                if flag:#如果标志位为真
                    if not has_write:#如果标志位为真；不为假；即为真
                        for new_line in fetch_list:#定义循环；循环fetch_list中剩余的字符串
                            temp = "%s%s\n" % (" " * 8, new_line)# 给字符串前加上8个空格
                            write_obj.write(temp)#将处理好的字符串写入新的配置文件
                        has_write = True#定义标志位为真；fetch_list中的内容是否重新写入到了文件
                else:
                    write_obj.write(line)#将原配置文件写入新配置文件
    else:
        return
    os.rename("ha.txt","ha.txt.bak")#将原配置文件备份
    os.rename("ha.new","ha.txt")#将新配置文件更名为原配置文件名


del_speiido = '{"backend": "www.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}'
del_dict = json.loads(del_speiido)#将json编码的字符串再转换为python的数据结构
#delete(del_dict)
#定义起始文件
if __name__ == '__main__':
    #提示信息
    print("1、获取文件\n2、添加文件\n3、删除文件")
    abcde = input("请输入你的选择：")
    if abcde == "1":
        print(999999999)
        a1= input("请输入backend：如buy.oldboy.org：")
        a2 = fetch(a1)#想找到buy.oldboy.org
        for a3 in a2:
            print(a3)
    elif abcde == "2":
        print("添加数据")
        add1(app_dict)
    elif abcde == "3":
        print("删除数据")
        delete(del_dict)
    else:
        print("输入错误请重新输入：")










