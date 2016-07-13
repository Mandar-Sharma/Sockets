#Org 9010
from socket import *
from threading import Thread
from SocketServer import ThreadingMixIn

host = "192.168.64.1"

class ClientThread(Thread):

    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print "Thread started for "+ip+":"+str(port)

    def run(self):
        with open('received_file', 'wb') as f:
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

s_file = socket(AF_INET, SOCK_STREAM)
port_file = 8080
s_file.bind((host,port_file))
threads= []

s_file.listen(5)
while True:
    (conn,(ip,port)) = s_file.accept()
    print 'Received connection from ', (ip,port)
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()