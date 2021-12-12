import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
socket.AF_INET6：ipv6
socket.AF_INET：ipv4
socket.SOCK_STREAM：TCP协议
socket.SOCK_DGRAM：UDP协议
"""
ip = "192.168.1.5"
port = 6000
# 绑定ip与端口（0~65535）
soc.bind((ip, port))

# 设置可监听的客户端为5个,可不填数值表示没有限制
soc.listen(5)
# 等待客户端连接，返回客户端对象与地址
client, address = soc.accept()

# 向客户端发送的消息，发送的字符串必须编码
str = "客户端，你好"  # 要发送的消息内容
client.send(str.encode('utf8'))

# 接收客户端发送的消息，每次最多接收1024个字节
# 接收到的消息，也必须解码才能正常显示
msg = client.recv(1024).decode('utf8')
# 打印接收到的消息和客户端的地址
print(f"来自客户端的消息：{msg}\n客户端地址{address}")
while True:
    # 接收消息
    msg01 = client.recv(1024).decode('utf8')
    print(f"客户端发来：{msg01}")
    if msg01 == '退出':
        client.send('退出双端'.encode('utf8'))
        break
    # 发送消息
    send_msg = input("回复客户端：")
    client.send(send_msg.encode('utf8'))
