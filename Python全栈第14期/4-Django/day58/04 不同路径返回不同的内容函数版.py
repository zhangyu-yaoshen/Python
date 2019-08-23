"""
使用socket 搭建一个简单的web服务端
函数版
"""

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


while 1:
    conn, addr = sk.accept()
    data = conn.recv(9000)
    # 把收到的字节类型的数据转换成字符串
    data_str = str(data, encoding='utf8')
    # 按照课前练习切分字符串，得到请求行
    first_line = data_str.split('\r\n')[0]
    # 对请求行按照空格切割
    url = first_line.split(' ')[1]
    print(url)
    if url == '/yingying/':
        msg = yingying(url)
    elif url == '/hpg/':
        msg = hpg(url)
    else:
        msg = b'404 not found!'
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    conn.send(msg)
    conn.close()
