"""
1. http://autohome.com.cn/
   代码发送GET请求

2. 接收返回值： 响应头+响应体

3. 获取响应体解析，方便的获取内容
"""
import requests
from bs4 import BeautifulSoup


# response = requests.get("http://www.autohome.com.cn/news/")
# response.status_code
# response.cookies
# response.headers
# response.content # 字节类型
# response.text    # 字符串
# print(response.text)
# response.encoding = 'gbk'
# print(response.text)

# 标签对象
# obj = BeautifulSoup(response.text,'html.parser')
#obj.find('div',attrs={'id':"auto-channel-lazyload-article",'class':'xxxxx'})
# obj.find(id="auto-channel-lazyload-article",_class='fff')
# 标签对象
# tag = obj.find(name='div',id='auto-channel-lazyload-article')
# # [标签对象,]
# tag = obj.find_all(name='div',id='auto-channel-lazyload-article')
# tag[0].


# 示例
response = requests.get("http://www.autohome.com.cn/news/")
response.encoding = 'gbk'
root = BeautifulSoup(response.text,'html.parser')
outer_div_obj = root.find(name='div',id='auto-channel-lazyload-article')
li_obj_list = outer_div_obj.find_all(name='li')
for li_obj in li_obj_list:
    if not li_obj.find('h3'):
        continue
    title_obj = li_obj.find('h3')
    summary_obj = li_obj.find('p')
    img_obj = li_obj.find('img')
    src = img_obj.attrs.get('src')
    print(src,title_obj.text,summary_obj.text)
    # 下载图片
    # img_response = requests.get(src)
    # img_file_name = src.rsplit('/', maxsplit=1)[1]
    # with open(img_file_name,'wb') as f:
    #     f.write(img_response.content)












