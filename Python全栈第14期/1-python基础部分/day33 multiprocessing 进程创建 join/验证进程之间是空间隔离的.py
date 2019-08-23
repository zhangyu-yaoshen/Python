import time
from multiprocessing import Process

#进程之间是空间隔离的,不共享资源
# global_num = 100
# def func1():
#     global global_num
#     global_num = 0
#     print('子进程全局变量>>>',global_num)
#
# if __name__ == '__main__':
#     p1 = Process(target=func1,)
#     p1.start()
#     time.sleep(1)
#     print('主进程的全局变量>>>',global_num)


def func1(n):
    print('>>>',n)

if __name__ == '__main__':
    #两种传参方式:
    # p1 = Process(target=func1,args=(1,))
    p1 = Process(target=func1,kwargs={'n':1})
    p1.start()
    print('主进程结束')








