import socket
udp_client = socket.socket(type=socket.SOCK_DGRAM)
server_ip_port = ('192.168.15.113',8001)

udp_client.sendto(b'hello',server_ip_port)

from_server_msg,server_addr = udp_client.recvfrom(1024)
print(from_server_msg)
print(server_addr)

udp_client.close()
