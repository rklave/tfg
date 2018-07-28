

# data Sender
import socket

host = "127.0.0.1" # set to IP address of target computer
port = 80
addr = (host, port)
s = socket(socket.AF_INET, socket.SOCK_DGRAM)
s.listen()
while True:
    #send the data here
    UDPSock.sendto(data, addr)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)