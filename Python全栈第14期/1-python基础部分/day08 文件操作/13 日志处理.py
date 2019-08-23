
result = []
with open("2018-09-12.log", mode="r", encoding="utf-8") as f:
    hang = f.readline()
    title = hang.split("|")
    for line in f:
        line = line.strip()  # 去掉空白, 2018-09-11 00:00:01|刘伟|吃鸡
        lst = line.split("|")
        #dic = {"时间": lst[0], "姓名": lst[1], "动作": lst[2]}
        dic = {title[0]: lst[0], title[1]: lst[1], title[2]: lst[2]}
        result.append(dic)
print(result)
