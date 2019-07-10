import socket
import struct
import os
import json

tcp_client = socket.socket()
server_ip_port = ('127.0.0.1',8001)
tcp_client.connect(server_ip_port)
read_size = 1024

file_info = {
    'file_path':r'D:\python_workspace\day031 ftp功能讲解+操作系统\bbb.mp4',
    'file_name':'bbb.mp4',
    'file_size':None,
}

#获取文件大小
file_size = os.path.getsize(file_info['file_path'])

#将文件大小添加到文件信息的字典中
file_info['file_size'] = file_size
#因为我们要发送的数据是字节类型,那么必须将字典转换为bytes类型,但是字典不能直接转换为bytes,所以我们想到了json,
#通过json模块将字典类型的文件信息数据转换为了json类型的字符串
file_info_json = json.dumps(file_info)
#获取了字符串的长度
file_info_len = len(file_info_json)
#将长度打包为4个字节的数据,
file_info_stru = struct.pack('i',file_info_len)
#将打包好的4个自己的数据和我的文件信息数据一起发送给了服务端
tcp_client.send(file_info_stru)
tcp_client.send(file_info_json.encode('utf-8'))

#统计文件数据
all_file_data = b''
#统计文件数据长度
all_size_len = 0

with open(file_info['file_path'],'rb') as f:

    while all_size_len < file_size:
        every_read_data = f.read(read_size)
        all_file_data += every_read_data
        #每次接受的长度的累加结果
        all_size_len += len(every_read_data)
        #发送每次读取的数据
        tcp_client.send(every_read_data)
        #得到一个百分比的浮点数
        percent_data = int(all_size_len/file_size* 100)
        print('\r%s%% %s'%(percent_data,'>'*(int(percent_data/5))) ,end='')



print(tcp_client.recv(1024).decode('utf-8'))
tcp_client.close()














