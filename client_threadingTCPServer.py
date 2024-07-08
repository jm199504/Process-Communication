import socket

host = '127.0.0.1'
port = 9999
addr = (host,port)

buff_size = 1024
# 建立套接字
s = socket.socket()
# 发送连接请求
s.connect(addr)
# 如果连接失败会报错如下
# ConnectionRefusedError: [WinError 10061] 由于目标计算机积极拒绝，无法连接。

while True:
    print('与服务器连接成功！')
    date = input('请输入您想发送给服务器的数据：').encode('utf-8')
    if not date or date == 'exit':
        break
    s.sendall(date)
    content = s.recv(buff_size)
    if not content:
        break
    print('服务器回复：' + content.decode('utf-8'))
s.close()

