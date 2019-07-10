import os # 引入os模块
#打开两个文件；设置变量f1和f2
with open("alex", mode="r", encoding="utf-8") as f1, \
     open("alex_副本", mode="w", encoding="utf-8") as f2:
    #读取f1文件
    for line in f1:
        #把所有sb换成good
        new_line = line.replace("sb", "good")
        #把改好的文件写到f2
        f2.write(new_line)
os.remove("alex")
os.rename("alex_副本", "alex")
