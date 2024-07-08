import socket
host = '127.0.0.1'
port = 9008
#AF_INET---IP4协议,套接字类型（流式）
s = socket.socket()#参数为全空---tcp套接字
s.bind((host,port))  #传入参数类型--元组且内数据不可改变  a = (1,2,3)
s.listen(5) #当前socket服务端最多可以接受8个客户端的连接

while True:#一旦建立连接之后不断等待连接
    # accept 阻塞，如果没有客户端请求一直等待
    conn,addr = s.accept()  #返回值为一个元组（conn-构建的一个套接字对象，用于接受和发送的对象，addr-连接客户端的对象）
    print('连接的客户端主机地址为：%s' % str(addr) )
    while True:#一旦连接建立之后不断保持发送和接受数据的状态
        text = conn.recv(1024)#参数为接受最大数据量（单位：字节）
        if len(text.strip())==0:#传来数据为空或者多个空格
            print('服务端接收到客户端的数据为空')
        else:
            print('接受客户端发来的消息为：%s' %(text.decode('utf-8')))
            content = input('请输入您要发送给客户端的数据：')
            conn.sendall(content.encode('utf-8'))#send  数据类型规定要字节类型
            print('\n')
    conn.close()

