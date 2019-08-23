"""
使用socket 搭建一个简单的web服务端
"""

import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

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
        msg = b'hands up!'
    elif url == '/hpg/':
        msg = b'computer is beitoule!'
    else:
        msg = b'404 not found!'
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    conn.send(msg)
    conn.close()
