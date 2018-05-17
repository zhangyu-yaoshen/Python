from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
#必须加参数；一般都用request【是请求信息对象】;HttpResponse【是响应信息对象】
def index(request):
    #返回一个字符串
    #return  HttpResponse("<h1>welcome python zhangyu</h1>")
    #返回页面;第一次参数是request；第二个参数是在templates目录下的文件；不需要导入；直接写就可以
    return render(request,"index.html")

def special_case_2003(request):
    return HttpResponse("qwer")

def year_archive(request,year):
    #这样写；url里输入什么就返回什么；127.0.0.1:8800/articles/2099/；返回2099
    return HttpResponse(year)

def month_archive(request,year,month):
    #返回年月
    return HttpResponse("year: %s    month: %s"%(year,month))

def article_detail(request,year,month,id):
    return HttpResponse(id)

def login(req):
    if req.method=='POST':
        username=req.POST.get('username',None)
        password=req.POST.get('pwd',None)
        if username=='alex' and password=='123':
            #return HttpResponse("登陆成功")
            #如果登录成功转到back的URL
            return redirect("/back")
    return render(req,'login.html')





import datetime
def timer(req):
    #当前时间
    t=datetime.datetime.now()
    #返回当前时间
    #return HttpResponse("<h1>Current time:%s</h1>" %t)
    #返回结果使用render渲染；
    """
    1、render会找到timer.html文件；
    2、在timer.html文件里找到{{}}在里面写Time；
        如：<h1>Current time: {{ Time }}</h1>
    """
    return render(req,"timer.html",{"Time":t})


#引用models模块
from blog.models import *

#ORM-查看数据
def back(req):
    #这里要注意在html文件里怎么去obg_list的值
    obg_list=Books.objects.all()
    #locals表示当前函数内的所有变量；在back文件里直接写{{name}}就可以
    return render(req,"back.html",locals())

#ORM-增加数据
def add_books(request):

    #创建记录的两种方式：1/create   2/save
    #注意：pub_date是Datetime数据类型；格式固定【2018-05-10】
    #Books.objects.create(title="python",author="egon",price=89,pub_date="2018-05-10")

    b=Books(title="JAVA",author="zhangyu",price=11,pub_date="2111-11-11")
    #调用save；保存到数据库
    b.save()
    #return HttpResponse("添加成功！！！")
    return redirect("/back/")


#ORM-删除数据
def delete_books(req):
    #取/delete_books?id=3里面的id
    id=req.GET.get("id")
    #filter帅选过滤;然后删除
    Books.objects.filter(id=id).delete()
    return redirect("/back/")

#ORM-编辑数据
def edit_books(req):
    id = req.GET.get("id")
    #filter和get都是筛选条件；filter取到的是集合对象；get是单一对象
    # b=Books.objects.get(id=id)
    # b.price=100
    # b.save()#效率低
    Books.objects.filter(id=id).update(price=100)
    return redirect("/back/")






