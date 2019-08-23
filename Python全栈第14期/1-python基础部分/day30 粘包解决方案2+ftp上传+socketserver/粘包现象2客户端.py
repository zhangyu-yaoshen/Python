import socket
import struct
client = socket.socket()
server_ip_port = ('192.168.15.113',8001)
client.connect(server_ip_port)
while 1:
    msg = input('请输入要执行的指令>>>')
    client.send(msg.encode('utf-8'))
    #先接收服务端要发送给我的信息的长度,前4个字节,固定的
    from_server_msglen = client.recv(4)
    unpack_len_msg = struct.unpack('i',from_server_msglen)[0]
    #接收数据长度统计,和服务端发给我的数据长度作比较,来确定跳出循环的条件
    recv_msg_len = 0
    #统计拼接接收到的数据,注意:这个不是统计长度
    all_msg = b''
    while recv_msg_len < unpack_len_msg:
        every_recv_data = client.recv(1024)
        #将每次接收的数据进行拼接和统计
        all_msg += every_recv_data
        #对每次接收到的数据的长度进行累加
        recv_msg_len += len(every_recv_data)

    print(all_msg.decode('gbk'))




