import socket

words = {
    '你的名字': '吕昊',
    '你的年龄': '21',
    '你好帅': '低调低调'
}
HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('服务器端口号：', PORT)
conn, addr = s.accept()
print("{}正在连接中...".format(addr))
while True:
    data = conn.recv(1024)
    data = data.decode()
    if not data:
        break
    print("收到消息：", data)
    conn.sendall(words.get(data, '没听懂').encode())
conn.close()
