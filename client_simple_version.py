import socket
host = '127.0.0.1'
port = 9008

s = socket.socket()
s.connect((host,port))
while True:
    text = input('请输入您要发送给服务器的数据：')
    s.sendall(text.encode('utf-8'))
    content = s.recv(1024)
    print('服务器发送来的数据：%s'%content.decode('utf-8'))
    print('\n')