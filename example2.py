# cliente UDP
import socket

#host = socket.gethostname()
host = '192.168.0.102'
port = 12346

server = ('192.168.0.118', 12345)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

file = open('.\Proves\outputC0.avi', 'rb')
bytes = file.read()
s.sendto(bytes, server)

s.close() 