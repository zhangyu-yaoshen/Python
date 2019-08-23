f = open("菜单", mode="w+", encoding="utf-8")  # 很少用.
f.write("疙瘩汤")
f.seek(0)   # 移动到开头
content = f.read()
print("读取的内容是", content)
f.flush()
f.close()