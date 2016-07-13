#Org 9010
#Courtesy of Mandar
#You're welcome :P

import json
from socket import *
from threading import Thread
from SocketServer import ThreadingMixIn

host = "192.168.64.1"

class ClientThread(Thread):

    def __init__(self, ip, port, sock, num):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        self.num = num
        print "Thread started for "+ip+":"+str(port)+"as no" + str(num)

    def run(self):
        with open('Rec2.txt', 'wb') as f:
            while True:
                print 'Receiving Data ... '
                data = conn.recv(9000)
                if not data:
                    break
                f.write(data)
        print 'Successfully Received'
        f.close()
        conn.close()
        print 'Connection Closed'
        fname = "RecFinal" + str(self.num)+".json"
        w = open(fname, 'w')
        dict = {}
        with open('Rec2.txt', 'r') as f:
            for line in f:
                for splita in line.split(';')[:-1]:
                    kv = splita.split(':')
                    dict[kv[0]] = kv[1]
                json.dump(dict, w)
        w.close()

s_file = socket(AF_INET, SOCK_STREAM)
port_file = 8080
s_file.bind((host,port_file))
threads= []

s_file.listen(5)
num = 1
while True:
    (conn,(ip,port)) = s_file.accept()
    print 'Received connection from ', (ip,port)
    newthread = ClientThread(ip, port, conn, num)
    newthread.start()
    threads.append(newthread)
    num += 1

for t in threads:
    t.join()