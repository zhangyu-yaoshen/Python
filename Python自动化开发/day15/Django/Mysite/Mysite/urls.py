"""Mysite URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
#应用blog下的views文件
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login,name="LOGIN"),
    #对应关系；调用views里的index函数【首页】【http://127.0.0.1:8800/blog/】
    url(r'^blog/', include('blog.urls')),
    url(r'^timer/',views.timer),
    url(r'^back',views.back),
    url(r'^add_books',views.add_books),
    url(r'^delete_books',views.delete_books),
    url(r'^edit_books',views.edit_books),
]
