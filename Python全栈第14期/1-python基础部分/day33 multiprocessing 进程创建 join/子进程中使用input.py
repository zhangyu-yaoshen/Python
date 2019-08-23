
from multiprocessing import Process

def func1():
    s = input('>>>')

if __name__ == '__main__':

    p1 = Process(target=func1,)
    p1.start()

    # a = input('>>>:')
    print('主进程结束')
