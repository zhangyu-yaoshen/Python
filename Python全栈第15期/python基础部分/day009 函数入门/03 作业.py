f = open("火锅", mode="r", encoding="utf-8")
result = []
for line in f: # name:apple price:10 amount:3 year:2012
    lst = line.split() # ['name:apple', 'price:10', 'amount:3', 'year:2012']
    dic = {}
    for el in lst: # 'name:apple'
        dic[el.split(":")[0]] = el.split(":")[1]
    result.append(dic)
print(result)