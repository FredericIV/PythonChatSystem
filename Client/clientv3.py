#Jeanette

import socket               # Import socket module
import _thread
import tkinter

hostname = socket.gethostname()

print("Type exit to exit")
s = socket.socket()         # Create a socket object
try:
   s.connect(('alarmpi', 4510))
except socket.error as msg:
   print("Fail on connection.")
   input("")
   exit()
e = socket.socket()
e.connect(('alarmpi', 4511))
def r1(randomis, threadname):
   while True:
      try:
         got = e.recv(1024)
      except socket.error as msg:
         exit()
      if not got:
         sys.exit(1)
      print((got + "\a"))
def send():
   if E1.get() == "exit":
      s.send("exit")
      s.close()
      e.close()
      exit()
   try:
      loss = E1.get()
      s.send(hostname + "-- " + loss)
   except socket.error as msg:
      exit()
_thread.start_new_thread(r1, ("world", "FredericIV"))
top = tkinter.Tk()
top.title("Chat Entry")
L1 = tkinter.Label(top, text="Say:")
L1.pack( side = "left" )
E1 = tkinter.Entry(top, relief="flat")
B = tkinter.Button(top, text ="Send", command = send)
B.pack( side = "right" )
E1.pack( fill="both" )
top.mainloop()
