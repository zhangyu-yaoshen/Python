import socket
client = socket.socket()
server_ip_port = ('192.168.15.113',8001)
client.connect(server_ip_port)
while 1:
    msg = input('请输入要执行的指令>>>')
    client.send(msg.encode('utf-8'))
    #先接收服务端要发送给我的信息的长度
    from_server_msglen = int(client.recv(1024).decode('gbk'))
    print('..........',from_server_msglen)
    #给服务端回应一个收到了你的信息长度的确认信息
    client.send('ok'.encode('utf-8'))

    #拿到信息长度后，将信息长度作为参数给了recv，recv就按照这个长度大小来接受服务端后面要给我发送的数据
    from_server_stdout = client.recv(from_server_msglen).decode('gbk')

    print('收到的正确信息:', from_server_stdout)

    # from_server_error = client.recv(1024).decode('utf-8')
    # print('收到的错误信息:',from_server_error)




