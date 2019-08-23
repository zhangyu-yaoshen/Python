import socket
#创建了一个socket对象
server = socket.socket()  #创建一个手机
ip_port = ('192.168.15.113',8001)  #创建了一张电话卡
#绑定IP地址和端口
server.bind(ip_port) #插上电话卡
#监听IP地址和端口

server.listen() #开机
print(11111)
#等待客户端的链接
conn, addr = server.accept()  #等着别人给我打电话,阻塞住

#接收消息
from_client_msg = conn.recv(1024) #1024为消息大小,单位B,MB = 1024KB,1KB = 1024B
#接收的消息是bytes类型,需要转换为字符串
from_client_msg = from_client_msg.decode('utf-8')
print(from_client_msg)

conn.send('死鬼,十点'.encode('utf-8'))
#关闭链接
conn.close()
server.close()

# print(conn)
# print('>>>>',addr)














