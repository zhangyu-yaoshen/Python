from django.shortcuts import render
import time
#缓存装饰器
from django.views.decorators.cache import cache_page
#缓存装饰器
@cache_page(10)
def index(request):
    ctime = time.time()
    return render(request,'index.html',{'ctime': ctime})

# 缓存
def home(request):
    ctime = time.time()
    return render(request, 'index.html', {'ctime': ctime})


def test(request):
    #调用自定义信号
    from s16day19 import pizza_done
    pizza_done.send(sender='xxxxx', toppings=123, size=456)


    return render(request,'test.html',{'n1': 123,'n2': "root"})