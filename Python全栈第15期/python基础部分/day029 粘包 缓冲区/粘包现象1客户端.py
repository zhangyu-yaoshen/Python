import socket
client = socket.socket()
server_ip_port = ('192.168.15.113',8001)
client.connect(server_ip_port)
client.send('hello'.encode('utf-8'))
client.send('sigui'.encode('utf-8'))

client.close()


#第二种粘包现象描述
#客户端第一次发送了一个2000B大小的数据
#第二次发送了一个1000B大小的数据
#由于服务的第一次接受数据的大小位1024B，导致剩余的976B的数据，在服务端第二次接受的数据中了
#根本原因：服务端不知道客户端发送数据的大小是多少










