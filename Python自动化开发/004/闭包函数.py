#!/usr/bin/env python
# -*- coding:utf-8 -*-
def f1():
    x=1
    def f2():#闭包函数
        print(x)
    return f2
f=f1()
x=9
f()

from urllib.request import urlopen
def page(url):
    def get():
        return urlopen(url).read()
    return get
baidu=page("http://m.88dushu.com/mulu/40326/")
print(baidu())


from urllib.request import urlopen
def page(url):
    def get():
        return urlopen(url).read()
    return get
baidu=page("http://m.88dushu.com/mulu/40326/")
print(baidu())