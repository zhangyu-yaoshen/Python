import time
import json
from django.shortcuts import render,HttpResponse,redirect
from app01 import models
from utils import BaseReponse
from app01 import forms
def index(request):
    news_list = models.News.objects.all()
    return render(request,'index.html',{'news_list': news_list})

def login(request):
    response = BaseReponse()
    try:
        obj = forms.LoginForm(request.POST)
        if obj.is_valid():
            # models.UserInfo.objects.filter(username=obj.cleaned_data['username'],pwd=obj.cleaned_data['pwd'])
            v = models.UserInfo.objects.filter(**obj.cleaned_data).first()
            if v:
                request.session['uuu'] = v.username
                response.status = True
            else:
                response.status = False
                response.error = "用户名或密码错误"
        else:
            print(obj.errors)
            response.status = False
            # response.error = "asdasdf"
            response.error = obj.errors
    except Exception as e:
        response.status = False
        response.error = '请求失败'
    return HttpResponse(json.dumps(response.__dict__, ensure_ascii=False))

def home(request):
    return render(request, 'home.html')

def logout(request):
    # 删除session；退出登录
    request.session.clear()
    return redirect('/index/')

def upload(request):
    #上传文件
    if request.method == "GET":
        return render(request,'upload.html')
    else:
        #获取上传文件的名
        obj = request.FILES.get('fffff')
        #在本地打开文件
        f = open(obj.name,'wb')
        #将上传的文件循环的写入本地
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        #上传完成后返回上传页面
        return render(request, 'upload.html')


def ajax_upload(request):
    import os
    response = BaseReponse()
    try:
        obj = request.FILES.get('fffff')
        file_path = os.path.join('static',obj.name)
        f = open(file_path, 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        response.status = True
        response.data = file_path
    except Exception as e:
        response.status = False
        response.error = "上传失败"
    print(file_path)
    return HttpResponse(json.dumps(response.__dict__))