import requests

r1 = requests.get('http://dig.chouti.com/')
r1_cookie_dict = r1.cookies.get_dict()

r2 = requests.post('http://dig.chouti.com/login',data={'phone': '8613121758648','password':'woshiniba','oneMonth':1},cookies=r1_cookie_dict)
print(r2)
r3 = requests.post('https://dig.chouti.com/link/vote?linksId=24472751',cookies=r1_cookie_dict)
print(r3.text)