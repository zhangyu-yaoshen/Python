f = open("疙瘩汤", mode="r+", encoding="utf-8")
# s = f.read(1) # 不管读多少.写依然是在末尾
# f.seek(0) # 移动到开头
# f.write("刘伟")
# f.seek(0,2) # 移动到末尾
# f.write("周星驰")
print(f.writable())
print(f.readable())
f.close()