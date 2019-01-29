"""
自动登录GitHub，获取个人信息
1. GET: https://github.com/session
   - 获取 authenticity_token

2. POST：
    commit:Sign in
    utf8:✓
    authenticity_token:7WZjQApL2MfuLizboZJG/QHrAlpJWdat14donOxvYxIy2eS4yYRw7PjaANkjUUmUYqmrTG4Hs90sQcArjakXTQ==
    login:asdf
    password:asdf

    响应内容Cookie

3. 获取个人信息
    携带cookie
"""
import requests
from bs4 import BeautifulSoup
import conf
# 第一次请求，获取 token
r1 = requests.get('https://github.com/login')
#获取整个标签页对象
b1 = BeautifulSoup(r1.text,'html.parser')
#获取 token【注意attrs和get取值】
authenticity_token = b1.find(name='input',attrs={'name': 'authenticity_token'}).get('value')
#print(authenticity_token)
#查看ri的cookies【.get_dict()已字典的形式】
#print(r1.cookies.get_dict())
r1_cookie_dict = r1.cookies.get_dict()

# 第二次请求，发送用户名和密码以及Token
r2 = requests.post('https://github.com/session',
                   data={
                       'commit': "Sign in",
                       'utf8':'✓',
                       'authenticity_token':authenticity_token,
                       'login':conf.USER,
                       'password':conf.PWD
                   },
                   #将第一次的cookies传送回去
                   cookies=r1_cookie_dict
                   )
r2_cookie_dict = r2.cookies.get_dict()

all_cookie_dict = {}
all_cookie_dict.update(r1_cookie_dict)
all_cookie_dict.update(r2_cookie_dict)
print(all_cookie_dict)

# 第三次请求：只有登录成功之后才能访问的页面
r3 = requests.get('http://github.com/settings/emails',cookies=all_cookie_dict)
print(r3.text)


























