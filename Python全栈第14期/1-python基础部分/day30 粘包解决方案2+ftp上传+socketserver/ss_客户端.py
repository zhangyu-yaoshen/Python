import socket

tcp_client = socket.socket()
server_ip_port = ('127.0.0.1',8001)
tcp_client.connect(server_ip_port)
while 1:
    client_msg = input('大阳哥>>>')
    tcp_client.send(client_msg.encode('utf-8'))
    from_server_msg = tcp_client.recv(1024).decode('utf-8')
    print(from_server_msg)


