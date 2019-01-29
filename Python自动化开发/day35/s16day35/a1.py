#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
1. http://autohome.com.cn/
   代码发送GET请求

2. 接收返回值： 响应头+响应体

3. 获取响应体解析，方便的获取内容
"""
import requests
from bs4 import BeautifulSoup

# #访问网站
# response = requests.get("http://www.autohome.com.cn/news/")
# #取状态
# response.status_code
# response.cookies
# response.headers
# #取内容【字节类型】
# response.content
# #把字节转换成字符串
# response.text
# #转换字符编码
# response.encoding = "gbk"
# print(response.text)
#
# #将整个网页信息等于obj变量信息【标签对象】
# obj = BeautifulSoup(response.text,"html.parser")
# #直接找第一个div标签；并且id是auto-channel-lazyload-article的
# obj.find("div",attrs={"id":"auto-channel-lazyload-article"})
# obj.find(id="auto-channel-lazyload-article")
# #【标签对象】
# tag = obj.find(name="div",id="auto-channel-lazyload-article")
# #【标签对象，】找所有
# tag = obj.find_all(name="div",id="auto-channel-lazyload-article")


response = requests.get("http://www.autohome.com.cn/news/")
#转换字符编码
response.encoding = "gbk"
root = BeautifulSoup(response.text,'html.parser')
#找第一个div标签；并且id是auto-channel-lazyload-article的
outer_div_obj = root.find(name='div',id='auto-channel-lazyload-article')
#找所有的li标签
li_obj_list = outer_div_obj.find_all(name='li')
#循环所有的li标签
for li_obj in li_obj_list:
    #如果不等于h3标签；就跳过
    if not li_obj.find('h3'):
        continue
    title_obj = li_obj.find('h3')
    summary_obj = li_obj.find('p')
    #过滤img标签
    img_obj = li_obj.find('img')
    #取img标签的src属性【<img src="//www2.autoimg.cn/newsdfs/g2/M06/91/1B/120x90_0_autohomecar__ChcCRFxOzUOAVb0sAAE7g2LYXYM994.jpg">】
    src = img_obj.attrs.get('src')
    #print(src,title_obj.text,summary_obj.text)
    # 下载图片
    #img_response = requests.get(src)

    #已/分割；取第一位置索引；得到【120x90_0_autohomecar__ChcCRFxOzUOAVb0sAAE7g2LYXYM994.jpg】
    img_file_name = src.rsplit('/', maxsplit=1)[1]
    img_response = requests.get(img_file_name)
    #打开文件img_file_name；并赋值给f
    with open(img_file_name,'wb') as f:
        #将字节类型写入
        f.write(img_file_name)





