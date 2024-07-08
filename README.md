### 基于Python实现进程间通信

#### 1. Socket介绍

Socket又称"套接字"，应用程序通常通过"套接字"向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。

socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口。在设计模式中，Socket其实就是一个门面模式，它把复杂的TCP/IP协议族隐藏在socket接口后面，对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议，表现形式：IP地址+Port端口。



#### 2. 大致流程（服务器）

①建立套接字socket：`socket.socket()`

②绑定主机和端口号：`bind(ip,port)`

③开启监听机制：`listent()`

④处于接受状态：`accept()`

⑤接收到连接请求，建立连接成功：`recv()`

⑥实现通信

⑦关闭通信：`close()`



#### 3. 大致流程（客户端）

①建立套接字：`socket.socket()`

②连接指定主机和端口号：`connect()`

③发送连接请求，建立连接成功：`send()`

④实现通信

⑤关闭通信：`close()`



#### 4. Python 提供了两个级别访问的网络服务

1. 低级别的网络服务支持基本的 Socket，提供了标准的 BSD Sockets API，可以访问底层操作系统Socket接口的全部方法。

2. 高级别的网络服务模块 SocketServer， 提供了服务器中心类，可以简化网络服务器的开发。



#### 5. 实现代码（低级别）

服务端：`server_simple_version.py`

客户端：`client_simple_version.py`



#### 6. 实现代码（高级别）

服务端：`server_threadingTCPServer.py`

客户端：`client_threadingTCPServer.py`



#### 6. socket的相关方法说明

绑定IP地址和端口到套接字：`socket.bind()`

开启TCP监听：`socket.listen()` 

被动接受TCP客户端的连接：`socket.accept()`

主动初始化TCP连接：`sockt.connect()`

connect函数的扩展，出错时返回错误码而不会抛出异常：`socket.connect_ex()`

 获取本地主机名：`socket.gethostname()` 

接受TCP数据：`socket.recv()`

发送TCP数据，返回值为发送字节数（可能小于string字节）：`socket.send()`

发送完整的TCP数据：`socket.sendall()`

指定远程地址，返回值也为发送字节数：`socket.sendto()`

返回套接字地址：`socket.getsockname()`

关闭套接字：`socket.close()`

设置套接字操作的超时期：`socket.settimeout()`
