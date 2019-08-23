#f = open("小护士模特少妇女网红.txt", mode="r", encoding="UTF-8")
#f = open("E:\Python\Python全栈第15期\python基础部分\day08 文件操作\小护士模特少妇女网红.txt", mode="r", encoding="UTF-8")
#content = f.read()  # 读取内容, 读取3个字符
#print(content)
# line1 = f.readline().strip() # 空白: 空格, \t, \n
# line2 = f.readline().strip()
# print(line1)
# print(line2)

# content = f.read()  # 一次全都读取出来. 缺点: 1. 读取大的文件的时候. 内存容易溢出 2. 操作比较麻烦

# content = f.readlines() # 也是全都加载进来了.
# print(content)


# f是一个可迭代对象
#f = open("d:/周润发大战奥特曼.txt", mode="r", encoding="utf-8") # 默认跟着操作系统走的  GBK
f = open("E:\Python\Python全栈第15期\python基础部分\day08 文件操作\小护士模特少妇女网红.txt", mode="r", encoding="UTF-8")
for line in f:  # 内部其实调用的是readline()
    print(line)
f.close() # 关闭


# 打印的末尾是换行
# print("哈哈")
# print("呵呵")
