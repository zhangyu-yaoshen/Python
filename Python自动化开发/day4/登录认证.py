#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
给一部分网页（函数）加登录认证需求
"""
def auth_deco(type):
    def auth(func):
        def wrapper(*args,**kwargs):
            username = input("Username:").strip()
            password = input("Password:").strip()
            if username == "zhangyu" and password == "123456":
                if type == "file":
                    print("\033[32;1mUser Has Passed Authentication\033[0m")
                    func(*args,**kwargs)
                elif type == "ldap":
                    print("这是ldap")
            else:
                exit("\033[31;1mInvalid Username Or Password\033[0m")
        return wrapper
    return auth
def index():
    print("这里是首页")
# @auth_deco("file")
# def home():
#     print("这里是本地文件")
@auth_deco("ldap")
def bbs():
    print("这里是LDAP")
index()
#home()
bbs()




















