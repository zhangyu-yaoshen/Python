import time
import time
from multiprocessing import Process
# 验证代码执行时间的
#   start_time = time.time()
#   代码执行逻辑
#   end_time = time.time()
#   print(end_time - start_time)

# 验证join方法
# global_num = 100
# def func1():
#     time.sleep(2)
#     global global_num
#     global_num = 0
#     print('子进程全局变量>>>',global_num)
# if __name__ == '__main__':
#     p1 = Process(target=func1,)
#     p1.start()
#     print('子进程执行')
#     #time.sleep(3)
#     p1.join()  #阻塞住,等待你的p1子进程执行结束,主进程的程序才能从这里继续往下执行
#     print('主进程的全局变量>>>',global_num)

#验证了一下并发的执行时间
# def fun1(n):
#     time.sleep(n)
#     print('func1',n)
# def fun2(n):
#     time.sleep(n)
#     print('fun2',n)
# def fun3(n):
#     time.sleep(n)
#     print('func3',n)

# if __name__ == '__main__':

    # p1 = Process(target=fun1,args=(1,))
    # p2 = Process(target=fun2,args=(2,))
    # p3 = Process(target=fun3,args=(3,))

    # p1.start()
    # p2.start()
    # p3.start()

#for循环在创建进程中的应用
def fun1(n):
    time.sleep(1)
    print(n)

if __name__ == '__main__':
    pro_list = []
    for i in range(10):
        p1 = Process(target=fun1,args=(i,))
        p1.start()
        # pro_list.append(p1)
        # p1.join()

    # for p in pro_list:
    #     p.join()
    p1.join()
    print('主进程结束')










#join方法







