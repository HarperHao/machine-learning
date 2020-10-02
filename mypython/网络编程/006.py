"""TCP客户端"""
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8888))
client_socket.sendall(b'hello')
#recv_data = client_socket.recv(1024)
#print('接受到的数据为：'.format(recv_data.decode()))
client_socket.close()
