import socket               # Import socket module
import thread
import Tkinter


s = socket.socket()         # Create a socket object
s.connect(('AlexAsus', 4503))


def r1(randomis, threadname):
   while True:
      got = s.recv(1024)
      if not got:
         sys.exit(1)
      print(got)
def send():
   if E1.get() == "exit":
      s.send("exit")
      s.close()
      exit()
   s.send(socket.gethostname() + "-- " + E1.get())
   print(E1.get())
thread.start_new_thread(r1, ("world", "FredericIV"))
top = Tkinter.Tk()
top.title("Chat Entry")
L1 = Tkinter.Label(top, text="Say:")
L1.pack( side = "left" )
E1 = Tkinter.Entry(top, relief="flat")
B = Tkinter.Button(top, text ="Send", command = send)
B.pack( side = "right" )
E1.pack( fill="both" )
top.mainloop()
