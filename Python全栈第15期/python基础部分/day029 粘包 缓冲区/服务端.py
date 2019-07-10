import socket
#创建了一个socket对象
server = socket.socket()  #创建一个手机

# server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  # 允许(IP地址和端口)地址重用

ip_port = ('192.168.15.113',8001)  #创建了一张电话卡

#绑定IP地址和端口
server.bind(ip_port) #插上电话卡
#监听IP地址和端口
server.listen() #开机,后面等待链接的客户端个数为3个
print(11111)

while 1:
    #等待客户端的链接,
    conn, addr = server.accept()  #等着别人给我打电话,阻塞住

    flag = 0
    while not flag:
        user_info = conn.recv(1024).decode('utf-8')  # alex|dsb
        print('客户端说>>>',user_info)
        if user_info == 'good|bye':
            break
        with open('account', 'r', encoding='utf-8') as f:
            for i in f:
                if i.strip() == user_info:
                    conn.send('登录成功'.encode('utf-8'))
                    flag = 1
                    break
            else:
                conn.send('用户名或者密码错误'.encode('utf-8'))


    # conn, addr = server.accept()

    print('准备断开连接！')

    conn.close()
# server.close()





# print(conn)
# print('>>>>',addr)














