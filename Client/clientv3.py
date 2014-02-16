import socket
import _thread
import tkinter
import time

hostname = socket.gethostname()
try:
   s = socket.socket()
   go = input("Where would you like to connect to? ")
   try:
      s.connect((go, 4510))
   except socket.error as msg:
      print("Fail on connection.")
      input("")
      exit()
   e = socket.socket()
   e.connect((go, 4511))
   def r1(randomis, threadname):
      while True:
         try:
            got = str(e.recv(1024), "utf-8")
         except socket.error as msg:
            exit()
         if not got:
            exit(1)
         print(got)
   def sender():
      if E1.get() == "exit":
         s.sendall(bytes("exit", "utf-8"))
         s.close()
         e.close()
         exit()
      try:
         loss = E1.get()
         google = str(time.strftime("%H:%M:%S") + " " + hostname + " --" + loss)
         s.sendall(bytes(google, "utf-8"))
      except socket.error as msg:
         exit()
   _thread.start_new_thread(r1, ("world", "FredericIV"))
   top = tkinter.Tk()
   top.title("Chat Entry")
   L1 = tkinter.Label(top, text="Say:")
   L1.pack( side = "left" )
   E1 = tkinter.Entry(top, relief="flat")
   B = tkinter.Button(top, text ="Send", command = sender)
   B.pack( side = "right" )
   E1.pack( fill="both" )
   top.mainloop()
finally:
   s.sendall(bytes("exit", "utf-8"))
   s.shutdown(socket.SHUT_RDWR)
   s.close()
   e.shutdown(socket.SHUT_RDWR)
   e.close()
   exit()
