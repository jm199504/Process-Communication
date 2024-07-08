
#socketserver   框架
#1、socketserver的StreamRequestHand类对象
#  服务端处理客户端发来的请求的一个类对象
#2、ThreadingTCPServer   异步通信引入到了我们的脚本文件 继承于baseserver
#3、分叉技术：用于实现多进程 unix/linux
#fork分叉函数是unix系统最杰出的成就之一
#对一个进程的堆栈段以及数据段 进行拷贝    （父进程）
#拷贝给子进程，使用相同的代码段
#一旦子进程开始运行，它内部的数据已经和父进程数据分开，相互之间不再有影响
#linux使用python代码创建fork分叉函数来创建多进程
#windows7    分叉技术是很难实现的
#windows使用多线程ThreadingTCPServer类对象

#socketserver有4个基础服务类
#TCPServer  tcp服务端
# UDPServer udp服务端
# UnixStreamServer  unix流式tcp
# UnixDategramServer    unix数据报udp

#总结socketserver创建一个服务端的过程与步骤
#1、用面向对象StreamRequestHandler（处理请求类） 继承于BaseRequestHandler（不需要写继承，可直接使用子类）
#handle()重写这个方法
#2、实例化一个server class对象，把StreamRequestHandler传入到server
#3、调用handle_request或者使用server_forever()

import socketserver
from socketserver import StreamRequestHandler as srh #请求处理类

host = '127.0.0.1'
port = 9999

class Request_Handle(srh):
    def handle(self):
        print('连接到服务端的客户端地址为：%s'%str(self.client_address))
        while True:
            date = self.request.recv(1024)
            if not date:
                break
            print('服务端接收到的数据为：%s'%date.decode('utf-8'))
            print('客户端地址为：%s:' % str(self.client_address))#
            content = input('请输入您想发送给客户端的数据：').encode('utf-8')
            self.request.send(content)

print('服务器开始运行！')
server = socketserver.ThreadingTCPServer((host,port),Request_Handle)#创建多线程代理
server.serve_forever()