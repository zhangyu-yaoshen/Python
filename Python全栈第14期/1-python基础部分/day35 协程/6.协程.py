# by luffycity.com
import greenlet
def f1():
    print(11)
    # 执行协程gr2
    gr2.switch()
    print(22)
    # 执行协程gr2
    gr2.switch()
def f2():
    print(33)
    # 执行协程gr1
    gr1.switch()
    print(44)
# 协程 gr1
gr1 = greenlet.greenlet(f1)
# 协程 gr2
gr2 = greenlet.greenlet(f2)
# 执行协程gr1
gr1.switch()