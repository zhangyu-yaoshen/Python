#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Name    : views.py
Author  : Python
Time    : 2019/8/21 0021 14:00
"""
# 返回一个页面
from django.shortcuts import render

def login(request):
    #访问login函数返回一个页面
    return render(request, "login.html")
