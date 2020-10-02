import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(sys.argv[1].encode(),("192.168.43.90" ,5000))
s.close()