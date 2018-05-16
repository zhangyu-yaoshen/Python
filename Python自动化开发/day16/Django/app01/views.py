from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    return HttpResponse("Index")

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








