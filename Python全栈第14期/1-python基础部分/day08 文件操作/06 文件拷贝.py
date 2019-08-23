f1 = open("戴蓝帽子的小白猫.jpg", mode="rb")
f2 = open("终极妖神.jpg", mode="wb")
# 读取f1；写入f2
for line in f1:
    f2.write(line)
f1.close()
f2.flush()
f2.close()