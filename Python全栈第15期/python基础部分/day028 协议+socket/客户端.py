import socket
client = socket.socket()

server_ip_port = ('192.168.15.113',8001)

#链接服务端
client.connect(server_ip_port)

while True:
    msg = input('明杰想说:')
    print('22222')
    #发消息
    client.send(msg.encode('utf-8')) #send里面的消息必须是字节类型的
    print('等待接收消息....')
    from_server_msg = client.recv(1024) #阻塞住,等待接收消息
    print('接收到了消息')
    from_server_msg = from_server_msg.decode('utf-8')
    print(from_server_msg)

client.close()


