"""模拟tftp客户端"""
from socket import *
import struct

s = socket(AF_INET, SOCK_DGRAM)
filename = "kebiao.png"
server_ip = '192.168.1.103'
send_data = struct.pack("!H10sb5sb", 1, filename.encode(), 0, b'octet', 0)
s.sendto(send_data, (server_ip, 69))
f = open('课表.png', 'ab')
while True:
    recv_data = s.recvfrom(1024)
    # print(recv_data)
    caozuoma, ack_num = struct.unpack('!HH', recv_data[0][:4])
    #print(caozuoma, ack_num)
    rand_port = recv_data[1][1]
    if int(caozuoma) == 5:
        print("文件不存在")
        break
    f.write(recv_data[0][4:])
    if len(recv_data[0]) < 516:
        break
    ack_data = struct.pack("!HH", 4, ack_num)
    s.sendto(ack_data, (server_ip, rand_port))
