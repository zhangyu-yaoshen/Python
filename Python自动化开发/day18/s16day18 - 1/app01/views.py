from django.shortcuts import render,HttpResponse
from app01 import models
#
# def create_temp_data(request):
#     for i in range(1,104):
#         models.UserInfo.objects.create(
#             username='root%s' %i,
#             password="123123",
#             email='root%s@qq.com' %i
#         )
#     return HttpResponse('创建成功')

def users1(request):

    from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
    current_page = request.GET.get('p')
    user_list = models.UserInfo.objects.all()

    #显示数据信息；只显示10条
    paginator = Paginator(user_list,10)
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    try:
        page_obj = paginator.page(current_page)
    # 如果错误返回首页
    except EmptyPage as e:
        page_obj = paginator.page(1)
    except PageNotAnInteger as e:
        page_obj = paginator.page(1)
    # has_next              是否有下一页
    # next_page_number      下一页页码
    # has_previous          是否有上一页
    # previous_page_number  上一页页码
    # object_list           分页之后的数据列表
    # number                当前页
    # paginator             paginator对象
    return render(request,'users1.html',{'page_obj':page_obj})


class PageInfo(object):
    def __init__(self,current_page,per_page_num):
        """
        :param current_page:  当前页
        :param per_page_num:  每页显示数据条数
        :param all_count:  数据库总个数
        :param base_url:  页码标签的前缀
        """
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = int(1)
        self.current_page = current_page
        self.per_page_num = per_page_num
        #self.all_count = all_count

#通过django分页
def users2(request):
    #当前页P【http://127.0.0.1:8000/users2?p=2】
    current_page = request.GET.get('p')
    current_page = int(current_page)

    per_page_num = 10
    #当前页减1乘以10
    start = (current_page - 1) * per_page_num
    # 当前页乘以10
    end = current_page * per_page_num

    #user_list = models.UserInfo.objects.all()[0:10]    # 1
    # user_list = models.UserInfo.objects.all()[10:20]   # 2
    # user_list = models.UserInfo.objects.all()[20:30]     # 3
    user_list = models.UserInfo.objects.all()[start:end]
    #user_list = models.UserInfo.objects.all()

    return render(request,'users2.html',{'user_list':user_list})

