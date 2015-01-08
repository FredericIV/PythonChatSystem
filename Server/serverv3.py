#!/usr/bin/python3
import socket
import _thread
import threading
import time
import queue


try: #My way of catching all errors gracefully
   print("Running...")

   s = socket.socket()
   s.bind(( '', 4510))
   s.listen(4)

   t = socket.socket()
   t.bind(( '', 4511))
   t.listen(4)
   print("Connected")
   globalmessage =  ""
   messagesServer = queue.Queue()
   
   innote = threading.Event()
   outnote = threading.Event()
   inlock = threading.Lock()
   spawncount = 0
   inbarrier = threading.Barrier(spawncount, )

   def r1(threadname, port): #Accepts handshakes and spawns a thread to receive communications.
      while True:
         c, addr = s.accept()
         _thread.start_new_thread(spawnedr1, (c, 4510))

   def spawnedr1(c, port): #Thread script that recive communications
      hostname=str(c.recv(1024), "utf-8")
      got = '{hostname} has entered the chatroom.'.format(hostname=hostname)
      global globalmessage
      global spawncount
      global inbarrier
      global inlock
      global innote
      global outnote
      globalmessage = got
      messagesServer.put(got)
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
            got = '{hostname} has exited the chatroom.'.format(hostname=hostname)
            globalmessage = got
            messagesServer.put(got)
            c.close()
            break
         inlock.acquire()
         inbarrier = threading.Barrier(spawncount, )
         globalmessage = str(time.strftime("%H:%M:%S") + " " + hostname + "-- " + got)
         messagesServer.put(str(time.strftime("%H:%M:%S") + " " + hostname + "-- " + got))
         innote.set()
         inbarrier.wait()
         innote.clear()
         outnote.set()
         inlock.release()

   def s1(threadname, port): #Accepts handshakes and spawns a thread to send messages.
      while True:
         d, addr = t.accept()
         _thread.start_new_thread(spawneds1, (d, 4510))

   def spawneds1(d, port): #Sends messages received
      global globalmessage
      global spawncount
      global inbarrier
      global inlock
      global innote
      global outnote
      spawncount += 1
      while True:
         try:
            innote.wait()
            d.sendall(bytes(globalmessage, "utf-8"))
            inbarrier.wait()
            outnote.wait()
         except socket.error as msg:
            d.close()
            break
      spawncount -= 1

   _thread.start_new_thread(r1, ("Frederic", 4510)) #Starts Spawners.
   _thread.start_new_thread(s1, ("Felicity", 4510))

   while True:
      print(messagesServer.get(True))
finally:
   try:
      s.shutdown(socket.SHUT_RDWR)
      s.close()
      t.shutdown(socket.SHUT_RDWR)
      t.close()
      exit()
   finally:
      exit()
