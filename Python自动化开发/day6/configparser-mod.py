#!/usr/bin/env python
# -*- coding:utf-8 -*-
import configparser
#生成configparser的实例
config = configparser.ConfigParser()
#生成[DEFAULT]字典；后面的字典就是参数
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

#生成['bitbucket.org']空字典
config['bitbucket.org'] = {}
#在['bitbucket.org']空字典中条件参数User = hg
config['bitbucket.org']['User'] = 'hg'

#生成['topsecret.server.com']空字典
config['topsecret.server.com'] = {}
#给['topsecret.server.com']空字典设置变量并添加值
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here

#给['DEFAULT']添加参数
config['DEFAULT']['ForwardX11'] = 'yes'

#将config值写道example.ini文件中
with open('example.ini', 'w') as configfile:
    config.write(configfile)



