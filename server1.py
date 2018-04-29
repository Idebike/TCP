#!/usr/bin/env python

import socket


TCP_IP = '10.200.0.209'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address: %s', addr)
server_on = 'yes'
while server_on == 'yes':
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print ("received data:%s", data)
        conn.send(data)  # echo

    
   server_on = input("Server 'on'/'off': ")
conn.close()
