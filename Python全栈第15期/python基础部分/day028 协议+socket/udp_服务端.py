import socket
#创建一个udp协议下的socket,需要使用参数type
udp_server = socket.socket(type=socket.SOCK_DGRAM) #DGRAM : datagram  数据报
#拿到一个地址,启动程序的时候,告诉电脑,你给我这个程序分配8001端口.
ip_port = ('192.168.15.113',8001)
#绑定IP地址和端口
udp_server.bind(ip_port)

print('准备接收消息了...')
#接收消息,from_client_msg来自客户端的消息,client_addr客户端的地址('192.168.15.113', 8001)
from_client_msg,client_addr = udp_server.recvfrom(1024)  #阻塞住了
print(11111)
print(from_client_msg)
print(client_addr)
#发送消息
udp_server.sendto(b'gunduzi',client_addr)
#关闭udp的socket对象
udp_server.close()


