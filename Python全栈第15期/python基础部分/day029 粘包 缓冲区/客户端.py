import socket
client = socket.socket()

server_ip_port = ('192.168.15.113',8001)
#链接服务端
client.connect(server_ip_port)

while 1:
    username = input('请输入用户名:')
    password = input('请输入密码:')
    # 按照服务端要求的信息格式发送
    user_info = username + '|' + password
    client.send(user_info.encode('utf-8'))
    if user_info == 'good|bye':
        break
    from_server_msg = client.recv(1024).decode('utf-8')
    print(from_server_msg)
    if from_server_msg == '登录成功':
        break

client.close()

