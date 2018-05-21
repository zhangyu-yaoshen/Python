from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method == "POST":
        #获取用户名和密码
        u = request.POST.get("user")
        p = request.POST.get("pwd")
        #查找数据库是否有用户名密码；【.first()生成对象】
        obj = models.UserInfo.objects.filter(username=u,password=p).first()
        #【.count()】获取个数；如果是0；就没有；不是0；就有
        #obj_count = models.UserInfo.objects.filter(username=u,password=p).count()
        #判断obj是否有数据
        if obj:
            return redirect("/index/")
        else:
            return render(request, "login.html")
    else:
        return redirect("/index/")

#引用models模块
from app01 import models
#创建数据
def orm(request):
    # 创建数据
    #models.UserInfo.objects.create(username="asdf",password="123",)
    #return HttpResponse("添加成功！！！")

    #查所有
    #result = models.UserInfo.objects.all()
    #查指定数据
    # result = models.UserInfo.objects.filter(username="root",password="123")
    # for row in result:
    #     print(row.id,row.username,row.password)

    #删除
    #models.UserInfo.objects.filter(id=2).delete()

    # 更新
    #models.UserInfo.objects.all().update(password="999")
    models.UserInfo.objects.filter(id="1").update(password="998889")


    return HttpResponse("添加成功！！！")















"""

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method == "POST":
        # #取得单选框的gender值；根据值判断选项
        # v = request.POST.get("gender")
        # print(v)
        # # 取得多选框的favor值；根据值判断选项；getlist获取多个值
        # v = request.POST.getlist("favor")
        # print(v)
        #上传文件；拿到的是文件名
        v = request.POST.get("fafafa")
        print(v)
        #上传的所有东西；都在request.FILES里
        obj = request.FILES.get("fafafa")
        print(obj,type(obj),obj.name)

        import os
        #在上传的文件名obj.name前边；加个路劲；
        file_path = os.path.join("upload",obj.name)
        #上传文件到指定路劲里
        f = open(file_path, mode="wb")
        #obj.chunks表示块；上传的东西一点一点上传
        for i in obj.chunks():
            #将上传的文件一点一点写到指定位置
            f.write(i)
        f.close()

        from django.core.files.uploadedfile import InMemoryUploadedFile

        return render(request, "login.html")
    else:
        return redirect("/index/")

"""



