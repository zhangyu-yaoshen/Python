from django.shortcuts import render, HttpResponse, redirect
from app01.models import User

def login(request):
    print(request.GET)
    print('-' * 120)
    error_msg = ''
    # 需要判断
    # 根据请求的方法来做判断
    if request.method == 'POST':
        # 如果是第二次来，表示填完了要给我发数据了             --> POST
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        print(email, pwd)
        # if email == '1@1.com' and pwd == '123':
        # 从数据库查询有没有这个用户
        # select * from app01_user where email='1@1.com' and pwd='123';
        ret = User.objects.filter(email=email, pwd=pwd)
        if ret:
            # 登录成功
            # 跳转到路飞学城
            # return redirect('https://www.luffycity.com')
            # return render(request, 'index.html')
            return redirect('/index/')
        else:
            # 登录失败
            # 提示用户邮箱或密码错误
            error_msg = '邮箱或密码错误'
    # 如果你是第一次来，是跟我要一个登录页面用来填写数据的  --> GET
    return render(request, 'login.html', {'error_msg': error_msg})


# def yingying(request):
#     # 拿到用户发过来的数据
#     print(request.POST)
#     # request.POST['email']
#     email = request.POST.get('email')
#     pwd = request.POST.get('pwd')
#     print(email, pwd)
#     if email == '1@1.com' and pwd == '123':
#         # 登录成功
#         # 跳转到路飞学城
#         # return redirect('https://www.luffycity.com')
#         # return render(request, 'index.html')
#         return redirect('/index/')
#     else:
#         # 登录失败
#         # 提示用户邮箱或密码错误
#         pass
#     return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')
