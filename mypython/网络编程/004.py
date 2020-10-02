"""udp广播"""
import socket

dest = ('<broadcast>', 7788)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(b'Hi', dest)
print('等待回复')
while True:
    (buf, address) = s.recvfrom(2048)
    print(address, buf.decode('GB2312'))
