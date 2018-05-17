from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    return HttpResponse("Index")
"""
def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method == "POST":
        u = request.POST.get("user")
        p = request.POST.get("pwd")
        if u == "alex" and p == "123":
            return redirect("/index/")
        else:
            return render(request, "login.html")
    else:
        return redirect("/index/")
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





