# servidor UDP
import socket
import struct
import pickle

print("Socket successfully created")
#host = socket.gethostname()
host = '192.168.0.118'
port = 12345
basename = "outputCR%s.avi"
videocounter = 0
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
print('connected: ', host, ' ', port)
payload_size = struct.calcsize("L")
while True:
   try:
      data = s.recvfrom(24576)
      print(str(data))
      myfile = open(basename % videocounter, 'wb')
      if not data:
         myfile.close()
         break
      myfile.write(data)
      myfile.close()
   except:
      s.close()
      continue
   videocounter += 1