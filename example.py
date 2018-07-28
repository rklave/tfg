# servidor UDP
import binascii
import socket
import uu

print("Socket successfully created")
#host = socket.gethostname()
host = '172.20.33.185'
port = 12345
basename = "outputCR%s.avi"
videocounter = 0
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
print('connected: ', host, ' ', port)

while True:
   try:
      data = s.recvfrom(24576)
      print(str(data[0]))
      myfile = open('sendOuput0.avi', 'wb')
      myfile.write(data[0])
      myfile.close()
   except:
      s.close()
      continue

s.close()