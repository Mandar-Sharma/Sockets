from socket import *
#AF_INET - IPv4
#SOCK_STREAM - TCP
#Localhost (Within System socket comm)
#host = socket.gethostname()
#192.168.64.1 - WLAN3-Connectify
s_file = socket(AF_INET,SOCK_STREAM)
host = "192.168.64.1"
#host = "localhost"
#port_file = 9010
port_file = 8080
s_file.bind((host,port_file))
#5 is backlog, no of pending connections to allow
s_file.listen(5)
while True:
          #s.accept blocks code until a connection is est
          #The server "Sleeps" if nothing is happening
          #s.accept returns a pair (client_socket,addr)
          #c is a new socket used for data/client socket
          #a is network/port address of clinet that connects
          c,a = s_file.accept()
          #using With, the file is close no matter how the nested loop is exited
          #Opens a file for writing only in binary format. Overwrites the file if the file exists.
          # If the file does not exist, creates a new file for writing.
          with open('received_file','wb') as f:
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
