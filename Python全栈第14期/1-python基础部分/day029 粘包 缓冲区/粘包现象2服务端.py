import socket
import subprocess

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
    sub_obj = subprocess.Popen(
        from_client_cmd, #客户端的指令
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    #接受到的返回信息是bytes类型的，并且windows系统的默认编码为gbk
    server_cmd_msg = sub_obj.stdout.read()
    # server_cmd_err = sub_obj.stderr.read().decode('gbk')
    cmd_msg_len = str(len(server_cmd_msg))
    print('指令返回的正确信息的长度>>>',cmd_msg_len)
    # print('指令返回的正确信息>>>',server_cmd_msg)
    # print('指令返回的错误信息...',server_cmd_err)

    conn.send(cmd_msg_len.encode('gbk'))

    from_client_ack = conn.recv(1024).decode('utf-8')
    print('from_client_ack',from_client_ack)
    if from_client_ack == 'ok':

        conn.send(server_cmd_msg)
    else:
        continue
    # conn.send(server_cmd_err.encode('utf-8'))






