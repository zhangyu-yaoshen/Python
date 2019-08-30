"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),#第一个login是URL；第二个是login函数
    url(r'^index/', views.index),
    url(r'^press_list/$', views.press_list),  # 展示出版社
    url(r'^add_press/$', views.add_press),  # 添加出版社
    url(r'^delete_press/$', views.delete_press),  # 删除出版社
    url(r'^edit_press/$', views.edit_press),  # 编辑出版社

    # ---------- day61 ↓ -------------------
    url(r'^book_list/$', views.jilei),  # 展示书籍
    url(r'^add_book/$', views.xiaojilei),  # 添加书籍
    url(r'^delete_book/$', views.delete_book),  # 删除书籍
    url(r'^edit_book/$', views.edit_book),  # 编辑书籍
]
