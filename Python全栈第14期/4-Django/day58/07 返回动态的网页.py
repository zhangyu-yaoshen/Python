"""
使用socket 搭建一个简单的web服务端
函数进阶版
"""
import time
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()


def yingying(url):
    data = 'ni fang wen de shi: {}'.format(url)
    return bytes(data, encoding='utf8')


def hpg(url):
    data = 'a huang de computer is bei tou le !'
    return bytes(data, encoding='utf8')


def login(url):
    # 返回一个字节类型HTML文件的内容
    with open('login.html', 'r', encoding='utf8') as f:
        data = f.read()
    now = str(time.time())
    data = data.replace('@@xx@@', now)
    return bytes(data, encoding='utf8')


# url和函数的对应关系
url_func = [
    ('/yingying/', yingying),
    ('/hpg/', hpg),
    ('/login/', login),
]


while 1:
    # ------------------- a。建立连接 接收消息部分 --------------------
    conn, addr = sk.accept()
    data = conn.recv(9000)

    # -------------------- b. 对用户发来的消息做处理的部分 -------------
    # 把收到的字节类型的数据转换成字符串
    data_str = str(data, encoding='utf8')
    # 按照课前练习切分字符串，得到请求行
    first_line = data_str.split('\r\n')[0]
    # 对请求行按照空格切割
    url = first_line.split(' ')[1]

    # --------------- c. 业务逻辑处理部分 ---------------------
    # 使用func变量保存将要执行的函数
    for i in url_func:
        if i[0] == url:
            func = i[1]
            break
    else:
        func = None
    # 执行函数
    if func:
        msg = func(url)
    else:
        msg = b'404 not found!'

    # ----------------- d. 回复响应消息 部分 ----------------------
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    conn.send(msg)
    conn.close()
