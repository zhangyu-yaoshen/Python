import socket
import struct
import json
import os
tcp_server = socket.socket()
ip_port = ('127.0.0.1',8001) #127.0.0.1本机的回环地址,供内部程序之间测试用的
tcp_server.bind(ip_port)
tcp_server.listen()
#客户端上传的文件路径,都放在这个路径下
client_file_path = r'D:\jj'
conn,addr = tcp_server.accept()
#首先接收到文件信息长度转换出来的4个字节的数据
file_info_stru = conn.recv(4)
#解包文件信息的长度
file_info_len = struct.unpack('i',file_info_stru)[0]
#然后接收文件的描述信息
client_file_info = conn.recv(file_info_len).decode('utf-8')
#将接收到的json字符串反序列化
abc_file_info = json.loads(client_file_info)
print('abc_file_info>>>',abc_file_info)
client_file_size = abc_file_info['file_size']
recv_all_size = 0
#拼接一下全路径
client_full_path = client_file_path + '\\' + abc_file_info['file_name']
# client_full_path = os.path.join(client_file_path,abc_file_info['file_name'])
with open(client_full_path,'wb') as f:
    while recv_all_size < client_file_size:
        every_recv_data = conn.recv(1024)
        f.write(every_recv_data)
        recv_all_size += len(every_recv_data)


conn.send('小伙玩的行,上传成功!'.encode('utf-8'))
conn.close()
tcp_server.close()


















