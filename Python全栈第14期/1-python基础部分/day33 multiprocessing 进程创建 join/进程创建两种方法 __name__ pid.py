import time
from multiprocessing import Process
import os
# import test01
# def func1(n):
#     # time.sleep(1)
#     print(n)
#
# def func2(n):
#     # time.sleep(1)
#     print(n)
#
# def func3(n):
#     # time.sleep(1)
#     print(n)
#
# def func4(n):
#     # time.sleep(1)
#     print(n)
#
# if __name__ == '__main__':
#     p1 = Process(target=func1,args=(1,))
#     p2 = Process(target=func2,args=(2,))
#     p3= Process(target=func3,args=(3,))
#     p4 = Process(target=func4,args=(4,))
#     p1.start() # run()
#     p2.start()
#     p3.start()
#     p4.start()
#     # time.sleep(0.5)
#     print('主进程结束')

    # 之前同步执行的
    # func1(1)
    # func2(2)
    # func3(3)
    # func4(4)

#创建进程的第一种方式:
    # p1 = Process(target=func1, args=(1,))
    # p1.start()
#创建进行的第二种方式:
    #自己定义一个类,继承Process类,必须写一个run方法,想传参数,自行写init方法,然后执行super父类的init方法

# class MyProcess(Process):
#     def __init__(self,n,name):
#         super().__init__()
#         self.n = n
#         self.name = name
#
#     def run(self):
#         # print(1+1)
#         # print(123)
#         print('子进程的进程ID',os.getpid())
#         print('你看看n>>',self.n)
#
# if __name__ == '__main__':
#     p1 = MyProcess(100,name='子进程1')
#     p1.start() #给操作系统发送创建进程的指令,子进程创建好之后,要被执行,执行的时候就会执行run方法
#     print('p1.name',p1.name)
#     print('p1.pid',p1.pid)
#     print('主进程结束')







