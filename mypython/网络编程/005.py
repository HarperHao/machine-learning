"""TCP多进程服务器"""
import socket
from multiprocessing import *
import time

def dealCustom(clent_socket):
    while True:
        data = clent_socket.recv(1024)
        if len(data) == 0:
            print("客户端断开连接")
            break
        else:
            print('客户端的数据:'.format(data))
            clent_socket.sendall('hello,我是服务器'.encode())
    clent_socket.close()


if __name__ == "__main__":
    servSockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servSockt.bind(('', 8888))
    servSockt.listen(5)
    try:
        # while True:
        #     print('主进程，等待客户到来')
        #     newSoc, address = servSockt.accept()
        #
        #     client = Process(target=dealCustom, args=(newSoc,))
        #     client.start()
        #     newSoc.close()
        newSoc, address = servSockt.accept()
        while True:
            data = newSoc.recv(1024)
            if len(data) == 0:
                print("客户端断开链接")
                break
            else:
                print('客户端的数据:'.format(data))
                #time.sleep(5)
                #newSoc.sendall('hello,我是服务器'.encode())
    finally:
        servSockt.close()
