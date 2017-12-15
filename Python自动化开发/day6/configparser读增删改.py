#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import configparser
# #生成configparser的实例
# config = configparser.ConfigParser()
# #读取配置文件
# config.read('example.ini')
# #查看配置文件内容
# print(config.sections())#显示['bitbucket.org', 'topsecret.server.com']
# #查看'bitbucket.org'是否在配置文件里
# print('bitbucket.org' in config)#True
#
# #给这个config['bitbucket.org']字典做变量
# b = config['bitbucket.org']
# print(b.keys())#KeysView(<Section: bitbucket.org>)
# print(list(b.keys()))#['user', 'serveraliveinterval', 'compressionlevel', 'compression', 'forwardx11']
#
# #循环这个字典；
# for k,v in b.items():print(k,v)
# """
# user hg
# serveraliveinterval 45
# compressionlevel 9
# compression yes
# forwardx11 yes
# """



# import configparser
# #生成configparser的实例
# config = configparser.ConfigParser()
# #读取配置文件
# config.read('example.ini')
# config.set('bitbucket.org',"name","zhangyu")
# config.write(open('example.ini',"w"))



# import configparser
# #生成configparser的实例
# config = configparser.ConfigParser()
# #读取配置文件
# config.read('example.ini')
# #remove_option删除单个参数【先写块的名字；后面谢要删哪行】
# config.remove_option("bitbucket.org","user")
# config.write(open('example.ini',"w"))




# import configparser
# #生成configparser的实例
# config = configparser.ConfigParser()
# #读取配置文件
# config.read('example.ini')
# #添加整块
# config.has_section("zhangyu")#查看是否有这个块
# config.add_section("zhangyu")#添加这个块
# config.write(open('example.ini',"w"))


import configparser
#生成configparser的实例
config = configparser.ConfigParser()
#读取配置文件
config.read('example.ini')
#修改User的值
config['bitbucket.org']['User'] = "zhangyu"
config.write(open('example.ini',"w"))

