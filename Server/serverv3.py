import socket
import _thread
import time
import queue

print("Running...")

s = socket.socket()
s.bind(( '', 4510))
s.listen(4)

t = socket.socket()
t.bind(( '', 4511))
t.listen(4)

messages = queue.Queue()
messages1 = queue.Queue()
messages2 = queue.Queue()
messages3 = queue.Queue()
messages4 = queue.Queue()
messagesServer = queue.Queue()

def r1(threadname, port):
   while True:
      c, addr = s.accept()
      while True:
         try:
            got = c.recv(1024)
         except socket.error as msg:
            c.close
         if got == "exit":
            c.close()
            break
         if not got:
            print ("\a")
         messages1.put(got)
         messages2.put(got)
         messages3.put(got)
         messages4.put(got)
         messagesServer.put(got)
def s1(threadname, port):
   while True:
      d, addr = t.accept()
      while True:
         try:
            d.send(messages1.get(True))
         except socket.error as msg:
            d.close()
def s2(threadname, port):
   while True:
      d, addr = t.accept()
      while True:
         try:
            d.send(messages2.get(True))
         except socket.error as msg:
            d.close()
def s3(threadname, port):
   while True:
      d, addr = t.accept()
      while True:
         try:
            d.send(messages3.get(True))
         except socket.error as msg:
            d.close()
def s4(threadname, port):
   while True:
      d, addr = t.accept()
      while True:
         try:
            d.send(messages4.get(True))
         except socket.error as msg:
            d.close()
_thread.start_new_thread(r1, ("Felicity", 4510))
_thread.start_new_thread(r1, ("Jeanette", 4510))
_thread.start_new_thread(r1, ("Drew", 4510))
_thread.start_new_thread(r1, ("Frederic", 4510))
_thread.start_new_thread(s1, ("Felicity", 4511))
_thread.start_new_thread(s2, ("Jeanette", 4511))
_thread.start_new_thread(s3, ("Drew", 4511))
_thread.start_new_thread(s4, ("Frederic", 4511))
while True:
   print(messagesServer.get(True))
