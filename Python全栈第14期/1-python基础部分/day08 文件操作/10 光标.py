f = open("菜单", mode="a+", encoding="utf-8")  # r+ a+ w+

# f.write("我要多写一点内容. 然后争取能看到效果")
# f.seek(0)
# print(f.read())
# f.seek(0)
# f.write("你")
#
# f.seek(0)
# print(f.read(1))
# f.seek(0)
# f.write("大米饭")
# f.write("大米粥")
# print(f.tell())
# f.seek(3) # 字节
# print(f.read(1))
# # print(f.read(1)) # 字符
# # print(f.read(1)) # 字符
# print(f.tell()) #字节
# 使用tell()可以知道光标在哪里
# seek()可以移动光标
# 读写的时候. 单位 字符
# 光标: 单位是字节
#  光标移动到末尾: seek(0,2)

# seek(偏移量, 位置)
# 位置: 0开头, 1当前位置, 2末尾
# 移动到末尾: seek(0, 2)





