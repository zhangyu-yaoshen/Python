import os
import time
from multiprocessing import Process



#父进程:子进程是在父进程的运行过程中开启的
#主进程

def func1():
    print('子进程',os.getpid())
    print('子进程的父进程',os.getppid())
    print(123)
    # time.sleep(10)

if __name__ == '__main__':
    # print('准备开始其他进程了')
    # print('主进程的父进程ID号>>>',os.getppid())
    # print('主进程的进程ID号>>>',os.getpid())
    #创建一个进程,target:我新创建的这个进程要去执行func1这个函数
    p1 = Process(target=func1,)
    #启动进程
    p1.start()
    print('到这里结束了')














