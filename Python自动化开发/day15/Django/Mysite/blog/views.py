from django.shortcuts import render,HttpResponse
# Create your views here.
#必须加参数；一般都用request【是请求信息对象】;HttpResponse【是响应信息对象】
def index(request):
    #返回一个字符串
    #return  HttpResponse("<h1>welcome python zhangyu</h1>")
    #返回页面;第一次参数是request；第二个参数是在templates目录下的文件；不需要导入；直接写就可以
    return render(request,"index.html")



