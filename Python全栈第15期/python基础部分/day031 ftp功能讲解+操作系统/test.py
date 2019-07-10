import threading
import time
def fun(n):
    time.sleep(2)
    print('>>>>',n)


if __name__ == '__main__':
    t = threading.Thread(target=fun,args=(13,))
    t.start()

    print('程序结束')




