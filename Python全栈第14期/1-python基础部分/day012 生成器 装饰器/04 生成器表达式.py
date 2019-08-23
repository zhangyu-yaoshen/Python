# 元组没有推导式
# [结果 for if]
# {key for if}
# {key:value for if}
# (结果 for if) # 生成器表达式, 拿到的是生成器

# 可以使用生成器表达式直接创建生成器
# gen = (i for i in range(10)) # generator
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())

# 生成器表达式: 记录一下代码。 然后每次需要的时候去生成器中执行一次这个代码
# 列表推导式: 一次性把所有的数据创建出来, 容易产生内存浪费
# 特性:
#     1. 节省内存
#     2. 惰性机制
#     3.只能向前。


# 生成器函数
# def func():
#     print(111)
#     yield 222
# g = func() #  生成器
# g1 = (i for i in g) # 生成器
# g2 = (i for i in g1) # 生成器
# print(list(g1)) # 222
# print(list(g2))
# print(list(g)) # 才会开始真正的取数据

# 计算两个数的和
def add(a, b):
    return a + b
# 生成器函数, 0-3
def test():
    for r_i in range(4):
        yield r_i
# 获取到生成器
g = test() # 惰性机制

for n in [2, 10, 5]:
    g = (add(n, i) for i in g)  # 循环的内部也是一个生成器
n = 2
g = (add(n, i) for i in g)
n = 10
g = (add(n, i) for i in (add(n, i) for i in g))
n = 5
g = (add(n, i) for i in (add(n, i) for i in (add(n, i) for i in test())))
g = (add(n, i) for i in (add(n, i) for i in (5,6,7,8)))
g = (add(n, i) for i in (10,11,12,13))
g = (15,16,17,18)
print(list(g)) # 刚开始拿数据
# 生成器记录的是代码


















