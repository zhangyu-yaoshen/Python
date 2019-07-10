f = open("我的天呐", mode="r+", encoding="utf-8")
f.seek(9)
f.truncate(12) # 如果没有参数. 按照光标来阶段. 如果有参数. 截断到参数位置
f.flush()
f.close()