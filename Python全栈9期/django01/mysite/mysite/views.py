#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render,HttpResponse

def yimi(request):#request参数保存了所有和用户浏览器请求相关的数据
    return HttpResponse("hello yimi!")
def xiaohei(request):#request参数保存了所有和用户浏览器请求相关的数据
    return HttpResponse("hello xiaohei!")
def login(request):
    return render(request, "login.html")