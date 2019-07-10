f = open("菜单", mode="r+", encoding="utf-8")  # r+最常见
s = f.read(1) # 读取一个字符
print(s)
f.write("胡辣汤") # r+模式. 如果你执行读了操作. 那么写操作的时候. 都是写在文件的末尾. 和光标没有关系
# f.write("ab") # 在文件开头写入. 写入的是字节,把原来的内容盖上

# for line in f:
#     print(line)
# f.write("蛋炒饭")
# 正确用法: 先读后写
f.close()