f = open("sylar.txt", mode="a", encoding="utf-8")
f.write("娃哈哈\n") # 追加写
f.write("爽歪歪\n")
f.flush()
f.close()
