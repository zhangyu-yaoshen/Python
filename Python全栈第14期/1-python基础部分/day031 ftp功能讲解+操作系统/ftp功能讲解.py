#进度条打印,print版
# import time
# for i in range(20):
#     #\r 回到行首打印内容,如果同一行有内容,那么就被抹掉了
#     n = '>' * i
#     print('\r%s' %n,end='')
#     time.sleep(0.5)

#进度条打印,sys版
# import sys
# import time
# for i in range(10):
#     sys.stdout.write('>')
#     sys.stdout.flush()
#     time.sleep(0.5)


#搞百分比的样子
#0.42857142857142855 改成两位数,不进行四舍五入
# print(3/7) #0.42857142857142855
# print(round(3/7,2)) #0.43  43%
# print(int(3/7*100))
















