import socket
import subprocess
import struct

server = socket.socket()
ip_port = ('192.168.15.113',8001)
server.bind(ip_port)
server.listen()
conn,addr = server.accept()
while 1:
    #来自客户端的指令
    print('等待接受信息。。。')
    from_client_cmd = conn.recv(1024).decode('utf-8')
    print(from_client_cmd)
    #通过subprocess模块执行服务端的系统指令,并且拿到指令执行结果
    sub_obj = subprocess.Popen(
        from_client_cmd, #客户端的指令
        shell=True,
        stdout=subprocess.PIPE, #标准输出:正确指令的执行结果在这里
        stderr=subprocess.PIPE, #标准错误输出:错误指令的执行结果在这里
    )
    #接受到的返回信息是bytes类型的，并且windows系统的默认编码为gbk
    server_cmd_msg = sub_obj.stdout.read()
    # server_cmd_err = sub_obj.stderr.read().decode('gbk')
    #首先计算出你将要发送的数据的长度
    cmd_msg_len = len(server_cmd_msg)
    #先对数据长度进行打包,打包成4个字节的数据,目的是为了和你将要发送的数据拼在一起,就好我们自定制了一个消息头
    msg_len_stru = struct.pack('i',cmd_msg_len)
    conn.send(msg_len_stru) #首先发送打包成功后的那4个字节的数据
    conn.sendall(server_cmd_msg) #循环send数据,直到数据全部发送成功









