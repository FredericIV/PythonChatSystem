import socket
import _thread
import time
import queue


try:
   if socket.gethostname() == "AlexAsus":
      print("Running...")

   s = socket.socket()
   s.bind(( '', 4510))
   s.listen(4)

   t = socket.socket()
   t.bind(( '', 4511))
   t.listen(4)

   globalmessage =  ""
   messagesServer = queue.Queue()

   def r1(threadname, port):
      while True:
         c, addr = s.accept()
         _thread.start_new_thread(spawnedr1, (c, 4510))

   def spawnedr1(c, port):
      while True:
         try:
            got = str(c.recv(1024), "utf-8")
         except socket.error as msg:
            c.close()
            break
         except:
            c.close()
            break
         if got == "exit":
            c.close()
            break
         global globalmessage
         globalmessage = got
         messagesServer.put(got)

   def s1(threadname, port):
      while True:
         d, addr = t.accept()
         _thread.start_new_thread(spawneds1, (d, 4510))

   def spawneds1(d, port):
      old = ''
      while True:
         try:
            if globalmessage != old:
               old = globalmessage
               d.sendall(bytes(globalmessage, "utf-8"))
         except socket.error as msg:
            d.close()
            break

   _thread.start_new_thread(r1, ("Frederic", 4510))
   _thread.start_new_thread(s1, ("Felicity", 4510))

   while True:
      print(messagesServer.get(True))
finally:
   s.shutdown(socket.SHUT_RDWR)
   s.close()
   t.shutdown(socket.SHUT_RDWR)
   t.close()
