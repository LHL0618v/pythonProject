import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "192.168.1.5"
port = 6000
# 连接对应的服务端ip和端口
soc.connect((ip, port))

# 接收服务端消息，一次最多接收1024个字节
msg = soc.recv(1024).decode('utf8')
print(f"来自服务端的消息：{msg}")

# 向服务端发送的消息，发送的字符串必须编码
str = "服务端，你好"  # 要发送的消息内容
soc.send(str.encode('utf8'))
while True:
    # 发送消息
    string = input("发给服务端:")
    soc.send(string.encode('utf8'))
    # 接收消息
    msg01 = soc.recv(1024).decode('utf8')
    print(f"服务端的回复：{msg01}")
    if msg01 == '退出双端':
        break

