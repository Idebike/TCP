#!/usr/bin/env python

import socket


TCP_IP = '10.200.0.209'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
conn.send("connection successful")
while True:
   data = conn.recv(BUFFER_SIZE)
   if not data: continue
   print ("received data ", data)
   if data =='close': break
   conn.send("ok")  # echo

print ("connection ended")
  
conn.close()
