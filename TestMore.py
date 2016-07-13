import json
from socket import *
s_file = socket(AF_INET,SOCK_STREAM)
host = "192.168.64.1"
port_file = 8080
s_file.bind((host,port_file))
s_file.listen(5)
while True:
          c,a = s_file.accept()
          with open('Rec2.txt','wb') as f:
            while True:
                print 'Receiving Data ... '
                data = c.recv(9000)
                if not data:
                    break
                f.write(data)
          print 'Successfully Received'
          f.close()
          c.close()
          print 'Connection Closed'
          break
w = open('RecFinal.json', 'w')
dict = {}
with open('Rec2.txt','r') as f:
    for line in f:
        for splita in line.split(';')[:-1]:
            kv = splita.split(':')
            dict[kv[0]]=kv[1]
        json.dump(dict,w)
w.close()
