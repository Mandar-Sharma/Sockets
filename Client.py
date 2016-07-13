#6000
#Outgoing Clinet Connection
from socket import *
s_file = socket(AF_INET,SOCK_STREAM)
#host = "192.168.64.1"
host = "192.168.1.70"
#host = "localhost"
port_file = 8080
s_file.connect((host,port_file))
filename = 'Text.txt'
#rb- readonly : Binary
f = open(filename, 'rb')
#1024 BufferSize
l = f.read(9000)
while (l):
    s_file.send(l)
    l = f.read(9000)
f.close()
s_file.close()
