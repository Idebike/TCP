import socket
import time
import signal
TIMEOUT = 5 # number of seconds your want for timeout

def interrupted(signum, frame):
    "called when read times out"
   # print 'interrupted!'
signal.signal(signal.SIGALRM, interrupted)

def input():
    try:
           # print 'You have 5 seconds to type in your stuff...'
            foo = raw_input()
            return foo
    except:
            # timeout
            return

TCP_IP = '10.200.0.209'
TCP_PORT = 5005
BUFFER_SIZE = 1024
mess = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
data = s.recv(BUFFER_SIZE)
print "received data ", data
while True:
	signal.alarm(TIMEOUT)
       	text = input()
        signal.alarm(0)
	s.send(text)
	if text == 'close': break
	data = s.recv(BUFFER_SIZE)
	if data == 'ok' : continue
s.close()

print "connection off"
