from django.shortcuts import render,HttpResponse
from app01 import models
#
# def create_temp_data(request):
#     for i in range(104,1040):
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

    paginator = Paginator(user_list,10)
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    try:
        page_obj = paginator.page(current_page)
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

#Django分页【现成的】
class PageInfo(object):
    def __init__(self,current_page,per_page_num,all_count,base_url,page_range=11):
        """
        :param current_page:  当前页
        :param per_page_num:  每页显示数据条数
        :param all_count:  数据库总个数
        :param base_url:  页码标签的前缀
        :param page_range:  页面最多显示的页码个数
        """
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = int(1)
        self.current_page = current_page
        self.per_page_num = per_page_num
        self.all_count = all_count
        self.base_url = base_url
        self.page_range = page_range

        #判断页数
        a,b = divmod(all_count,per_page_num)
        if b != 0:
            self.all_page = a + 1
        else:
            self.all_page = a


    # 开始页
    def start(self):
        return (self.current_page - 1) * self.per_page_num
    # 结束页
    def end(self):
        return self.current_page * self.per_page_num

    def page_str(self):
        """
        在HTML页面中显示页码信息
        :return:
        """
        page_list = []
        # 如果当前页小于等于1
        if self.current_page <=1:
            prev = '<li><a href="#">上一页</a></li>'
        else:
            prev = '<li><a href="%s?p=%s">上一页</a></li>' %(self.base_url,self.current_page-1,)
        page_list.append(prev)

        #判断首页
        if self.all_page <= self.page_range:
            start =1
            end = self.all_page + 1
        else:
            #如果当前页大于5
            if self.current_page > int(self.page_range/2):
                #如果当前页加5大于总页数
                if (self.current_page + int(self.page_range/2)) > self.all_page:
                    #显示最后页到最后页减11页的值
                    start = self.all_page - self.page_range
                    end = self.all_page + 1
                else:
                    #希望显示当前页左右各5各的数
                    start = self.current_page - int(self.page_range/2)
                    end = self.current_page + int(self.page_range/2) +1
            else:
                start = 1
                end =self.page_range +1

        #显示中间的页码1到11页
        #for i in range(1,self.all_page+1):
        for i in range(start,end):
            if self.current_page == i:
                #class="active"显示当前网页样式
                temp = '<li class="active"><a href="%s?p=%s">%s</a></li>' %(self.base_url,i,i,)
            else:
                #不是当前页的；正常显示
                temp = '<li><a href="%s?p=%s">%s</a></li>' %(self.base_url,i,i,)
            page_list.append(temp)

        #如果当前页大于所有页；
        if self.current_page >= self.all_page:
            nex = '<li><a href="#">下一页</a></li>'
        else:
            nex = '<li><a href="%s?p=%s">下一页</a></li>' % (self.base_url,self.current_page + 1,)
        page_list.append(nex)

        return "".join(page_list)

def users2(request):
    #当前数据的总个数
    all_count = models.UserInfo.objects.all().count()
    #每页十条【request.path_info显示当前URL】
    page_info = PageInfo(request.GET.get('p'),10,all_count,request.path_info)
    #从数据库取出所有数据
    user_list = models.UserInfo.objects.all()[page_info.start():page_info.end()]
    return render(request,'users2.html',{'user_list':user_list,'page_info': page_info})

