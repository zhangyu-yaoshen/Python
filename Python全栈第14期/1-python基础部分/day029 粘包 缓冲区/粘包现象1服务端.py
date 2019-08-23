import socket
server = socket.socket()
ip_port = ('192.168.15.113',8001)
server.bind(ip_port)

server.listen()

conn,addr = server.accept()

from_client_msg1 = conn.recv(1024).decode('utf-8')
#2000B -- 1024  976B  + 1000B
from_client_msg2 = conn.recv(1024).decode('utf-8')
#976+48 = 1024
print('msg1:',from_client_msg1)
print('msg2:',from_client_msg2)

conn.close()
server.close()




