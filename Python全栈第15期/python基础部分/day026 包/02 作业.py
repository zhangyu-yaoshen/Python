import re
from urllib.request import urlopen

def getContent(url):
    return urlopen(url).read().decode("gbk")
# # 爬取 http://www.dytt8.net/ 上的内容
url = "http://www.dytt8.net"
content = getContent(url)
# 准备正则
obj = re.compile(r"\[<a .*?>最新电影下载</a>\]<a href='(?P<second_url>.*?)'>.*?</a>", re.S)
second_obj = re.compile(r'<div id="Zoom">.*?译　　名(?P<yiming>.*?)<br />◎片　　名(?P<pianming>.*?)<br />.*?◎导　　演(?P<daoyan>.*?)<br />◎主　　演(?P<zhuyan>.*?)<br /><br />◎简　　介.*?<td .*?><a href="(?P<download>.*?)">', re.S)

it = obj.finditer(content)
for el in it:
    second_url = el.group("second_url")
    second_content = getContent(url+second_url)
    second_it = second_obj.finditer(second_content) # 拿到第二层通过正则匹配到的内容.
    print("************************************************************************")
    for second_info in second_it:
        print(re.sub("[\u3000]", "", second_info.group("yiming")))
        print(re.sub("[\u3000]", "", second_info.group("pianming")))
        print(re.sub("[\u3000]", "", second_info.group("daoyan")))
        print(re.split("<br />", re.sub("[\u3000]", "", second_info.group("zhuyan"))))
        print(re.sub("[\u3000]", "", second_info.group("download")))
