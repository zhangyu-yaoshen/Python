f = open("菜单", mode="a+", encoding="utf-8")
f.write("韭菜鸡蛋饺子")

f.seek(0)
content = f.read()
print(content)