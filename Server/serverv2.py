import socket
import thread
import Tkinter

s = socket.socket(); print "Server"
s.bind(( '', 4503))
s.listen(5)
c, addr = s.accept()

def r1(randomis, threadname):
   while True:
      got = c.recv(1024)
      if not got:
          print ("\a")
          sys.exit(1)
      print(got)
def send():
   c.send(socket.gethostname() + "-- " + E1.get())
   print(E1.get())
thread.start_new_thread(r1, ("world", "Felicity"))
top = Tkinter.Tk()
top.title("Chat Entry Server")
L1 = Tkinter.Label(top, text="Say:")
L1.pack( side = "left" )
E1 = Tkinter.Entry(top, relief="flat")
B = Tkinter.Button(top, text ="Send", command = send)
B.pack( side = "right" )
E1.pack( fill="both" )
top.mainloop()
