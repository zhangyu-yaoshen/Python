
# 队列: 先进先出.  First In First Out FIFO
# 栈: 先进后出. First In Last Out FILO
import queue
# q = queue.Queue() # 创建队列
# q.put("刘伟") # 放入元素
# q.put("大阳哥")
# q.put("吴佩琪")
#
# print(q.get())  # 获取元素
# print(q.get())
# print(q.get())
# # print(q.get()) # 阻塞了. 在等下一个元素, input()

# 装馒头的桶
# 1. 入栈
# 2. 出栈
# 属性:   1. 列表(容器) 2.大小（size） 3. 栈顶指针（下一个装元素的位置）
class StackFullError(Exception):
    pass
class StackEmptyError(Exception):
    pass
class Stack:
    def __init__(self, size):
        self.index = 0  #  栈顶指针
        self.size = size
        self.lst = []  # 容器

    def push(self, el):
        if self.index < self.size:  #  还没有装满
            self.lst.insert(self.index, el)
            self.index += 1
        else:   # 装满了
            raise StackFullError("the stack is full!")

    def pop(self):
        if self.index > 0:
            self.index -= 1
            return self.lst[self.index]
        else:
            raise StackEmptyError("the stack is empty!")

# 使用
# 1.实例化栈
s = Stack(5)
s.push("馒头1")
print(s.pop())
s.push("馒头2")
print(s.pop())
s.push("馒头3")
print(s.pop())
s.push("馒头4")
print(s.pop())
s.push("馒头5")
print(s.pop())
s.push("馒头6")
print(s.pop())
