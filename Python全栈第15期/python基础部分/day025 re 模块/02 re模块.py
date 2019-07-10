import re

# 1. findall 查找所有结果.
# lst = re.findall("a", "abcabcdefgabc")
# print(lst)
#
# # 2. finditer 查找到的结果返回迭代器
# it = re.finditer(r"\d+", "鑫姐28号又收入了5000块") # 28  5000
# for el in it: # 从迭代器中获取到的是分组的信息
#     print(el.group()) # 获取具体信息

# # 3. search() 查找. 如果查找到第一个结果. 就停止. 如果查不到结果就返回None
# ret = re.search("a", "abac")
# print(ret.group())

# # 4. match() 匹配
# ret = re.match("a", "bcda") # 从头开始找  ^
# print(ret.group())


#  5. 操作
#   split  切割. 按照正则切割.
# lst = re.split(r"[ab]", "abcdefghahahehedebade")
# print(lst)

#   sub 替换.
# result = re.sub("250", "__sb__", "alex250taibai250taihei250ritian250liuwei")
# print(result)

# result = re.subn("250", "__sb__", "alex250taibai250taihei250ritian250liuwei")
# print(result)

# obj = re.compile(r"\d+")
# lst = obj.findall("大阳哥昨天赚了5000块")
# lst2 = obj.findall("银行流水5000， 花了6000")
# print(lst)
# print(lst2)



# obj = re.compile(r"(?P<id>\d+)(?P<zimu>e{3})")
# ret = obj.search("abcdefg123456eeeee") # ((123456)(eee))
# print(ret.group())
# print(ret.group("id"))
# print(ret.group("zimu"))


# ret = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
# print(ret) # 这是因为findall会优先把匹配结果组⾥内容返回,如果想要匹配结果,取消权限即可
# ret = re.findall('www.(?:baidu|oldboy).com', 'www.oldboy.com') # ?: 当前的（）不分组
# print(ret) # ['www.oldboy.com']


# ret=re.split("sb","alexsbwusirsbtaibaisbliuwei")
# print(ret)



import re
from urllib.request import urlopen  # 打开一个链接. 读取源代码
import ssl
# ⼲掉数字签名证书
ssl._create_default_https_context = ssl._create_unverified_context


def getPage(url):
    response = urlopen(url) # 和网页链接
    return response.read().decode('gbk') # 返回正常的页面源代码. 一大堆HTML
# def parsePage(s): # s 是页面源代码
#     ret = re.findall('<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?'+
#         '<span class="title">(?P<title>.*?)</span>'+
#         '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>'+
#         '(?P<comment_num>.*?)评价</span>', s, re.S)
#     return ret # id,title, rating_num, comment_num
#
# def main(num):
#     url = 'https://movie.douban.com/top250?start=%s&filter=' % num
#     response_html = getPage(url) # response_html是页面源代码
#     ret = parsePage(response_html)
#     print(ret) # id,title, rating_num, comment_num


def parsePage(s):
     com = re.compile(
         '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?' +
                 '<span class="title">(?P<title>.*?)</span>'+
                 '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>'+
                 '(?P<comment_num>.*?)评价</span>', re.S)
     ret = com.finditer(s)
     for i in ret:
         yield {
             "id": i.group("id"),
             "title": i.group("title"),
             "rating_num": i.group("rating_num"),
             "comment_num": i.group("comment_num"),
         }
def main(num):
     url = 'http://www.dytt8.net/'
     response_html = getPage(url)
     print(response_html)
     # ret = parsePage(response_html)
     # # print(ret)
     # f = open("move_info7", "a", encoding="utf8")
     # for obj in ret:
     #     print(obj)
     #     data = str(obj)
     #     f.write(data + "\n")

main(1)

