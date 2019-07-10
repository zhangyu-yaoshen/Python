#作业简单讲解
# 1.时间戳转换为格式化时间的字符串

import time

while 1:
    t1 = time.time()
    print(t1)
    t1_stru = time.localtime(t1)


    print(time.strftime('%Y/%m/%d',t1_stru))
    t1_ss = time.strftime('%Y/%m/%d',t1_stru)
    time.sleep(10)
    client.send(t1_ss)



