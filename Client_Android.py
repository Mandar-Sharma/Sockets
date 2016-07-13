import os
from socket import *
import time

os.chdir("/storage/emulated/0/Project")

s = socket(AF_INET,SOCK_STREAM)
host = "192.168.64.1"
port = 9010
s.connect((host,port))
filename = 'Text.txt'
clock_start = time.clock()
time_start = time.time()
#rb- readonly : Binary
f = open(filename, 'rb')
#1024 BufferSize
l = f.read(1024)
while (l):
    s.send(l)
    print('Sent ', repr(l))
    l = f.read(1024)
f.close()
#s.close() vs shutdown - shutdown allows receiving pending data from sender
s.shutdown(SHUT_WR)
clock_end = time.clock()
time_end = time.time()

duration_clock = clock_end - clock_start
print 'clock:  start = ',clock_start, ' end = ',clock_end
print 'clock:  duration_clock = ', duration_clock

duration_time = time_end - time_start
print 'time:  start = ',time_start, ' end = ',time_end
print 'time:  duration_time = ', duration_time
