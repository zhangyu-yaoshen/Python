import requests # 网络请求

rs = requests.get("http://pic.netbian.com/uploads/allimg/190706/221551-1562422551faab.jpg")
f = open("壁纸.jpg", mode="wb")
f.write(rs.content)
f.flush()
f.close()


# f = open("../b/破文件",mode="r", encoding="utf-8")
# s = f.read()
# print(s)

