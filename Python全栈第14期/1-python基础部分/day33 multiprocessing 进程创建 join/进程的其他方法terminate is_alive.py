import time
from multiprocessing import Process

def func1():
    time.sleep(2)
    print()
    print('子进程')

if __name__ == '__main__':
    p1 = Process(target=func1,)
    p1.start()

    p1.terminate() # 给操作系统发了一个关闭p1子进程的信号,关闭进程
    time.sleep(1)
    print('进程是否还活着:',p1.is_alive())
    print(p1.pid)
    print('主进程结束')



