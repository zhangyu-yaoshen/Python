
import time
import os
from multiprocessing import Process

def func1():
    time.sleep(5)
    print(os.getpid())
    print('子进程')

if __name__ == '__main__':
    p1 = Process(target=func1,)

    #将p1子进程设置为守护进程
    p1.daemon = True

    p1.start()

    # print('主进程的ID',os.getpid())
    print('主进程结束')





