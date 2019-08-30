from django.shortcuts import render, HttpResponse, redirect
from app01.models import User, Press


def login(request):
    # print(request.GET)
    # print('-' * 120)
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
        print(type(ret[0]))
        print(ret[0].id, ret[0].email, ret[0].pwd)
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


# ------------- day60 ↓ ----------------------
# 出版社列表处理函数
def press_list(request):
    # 1. 去数据库查所有的出版社
    ret = Press.objects.all().order_by('id')
    # print(ret)
    # print(ret[0])
    # print(ret[0].name)
    # 2. 在HTML页面上展示出来
    return render(request, 'press_list.html', {'kangchen': ret})


# 添加出版社的处理函数
def add_press(request):
    if request.method == 'POST':
        # 表示用户填写完了，要给我发数据
        # 1. 取到用户填写的出版社数据
        press_name = request.POST.get('name')
        # 2. 将数据添加到数据库中
        Press.objects.create(name=press_name)
        # 3. 跳转到出版社列表页面
        return redirect('/press_list/')

    # 1. 返回一个添加页面，让用户在上面填写新的出版社的信息
    return render(request, 'add_press.html')


# 删除出版社处理函数
def delete_press(request):
    # 1. 获取要删除的出版社ID
    delete_id = request.GET.get('id')
    print('-' * 120)
    print(delete_id)
    print('*' * 120)
    # 2. 根据id去数据库删除对应的数据行
    Press.objects.filter(id=delete_id).delete()
    # 3. 让用户再去访问以下出版社列表页
    return redirect('/press_list/')


# 编辑出版社
def edit_press(request):
    # 1. 从URL中获取要编辑的出版社的id
    edit_id = request.GET.get('id')

    if request.method == 'POST':
        # 用户修改完出版社数据给我发过来了
        # 1.取出用户编辑之后的数据
        new_name = request.POST.get('name')
        # 2. 去数据库修改对应的数据
        # 2.1 先找对应的数据：出版社对象
        edit_press_obj = Press.objects.get(id=edit_id)
        # 2.2 修改出版社的名称
        edit_press_obj.name = new_name
        # 2.3 将修改同步到数据库
        edit_press_obj.save()
        # 3. 让用户再去访问出版社列表页
        return redirect('/press_list/')

    # 2. 获取该出版社的信息
    # ret = Press.objects.filter(id=edit_id)  # -->[Press obj, ]
    # print(ret)
    # print('#' * 120)
    ret = Press.objects.get(id=edit_id)  # --> Press Obj, get()有且只能找到一个对象，否则就报错
    print(ret)
    # 3. 在页面上展示出来
    return render(request, 'edit_press.html', {'press_obj': ret})














