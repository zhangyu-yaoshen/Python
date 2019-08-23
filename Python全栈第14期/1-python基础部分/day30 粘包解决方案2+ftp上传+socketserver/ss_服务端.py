
import socketserver

#1 定义一个类
class MyServer(socketserver.BaseRequestHandler): #2 类里面继承socketserver.BaseRequestHandler
    # 3 类里面定义一个handle方法,handle名称不能变
    def handle(self):
        while 1:
        # self.request      #conn链接通道
            from_client_data = self.request.recv(1024).decode('utf-8')
            print(from_client_data)
            server_input = input('明巍sb说>>>')
            self.request.send(server_input.encode('utf-8'))
        # self.request.close()
if __name__ == '__main__':
    #服务端的IP地址和端口
    ip_port = ('127.0.0.1',8001)
    socketserver.TCPServer.allow_reuse_address = True
    #绑定IP地址和端口,并且启动我定义的上面这个类
    server = socketserver.ThreadingTCPServer(ip_port,MyServer)
    #永久的给我执行下去
    server.serve_forever()



