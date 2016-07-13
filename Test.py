from socket import *
s_file = socket(AF_INET,SOCK_STREAM)
host = "192.168.64.1"
port_file = 8080
s_file.bind((host,port_file))
s_file.listen(5)
co = 1
while True:
          c,a = s_file.accept()
          f = open('Rec.txt','wb')
          flow = True
          while flow:
              data = c.recv(9000)
              co = co + 1
              print "The current count is "
              print co
              print type(data)
              data_l = data.split(' ')
              for item in data_l:
                  f.write(item)
              if co == 3:
                  print "Count Reached"
                  f.close()
                  flow = False
          c.close()
          print 'Connection Closed'
