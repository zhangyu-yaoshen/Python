import time
import os
from multiprocessing import Process

def func1():
    time.sleep(30)
    print(os.getpid())
    print('子进程')

if __name__ == '__main__':
    p1 = Process(target=func1,)
    p1.start()
    # p1.join()
    # time.sleep(2)
    # print(p1.pid)
    print('主进程的ID',os.getpid())
    print('主进程结束')



