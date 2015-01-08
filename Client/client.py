version = "1.0.0"

import socket               # Import socket module
import sys
s = socket.socket()         # Create a socket object
s.connect(('AlexAsus', 4500))
s.send(socket.gethostname())
print "Type exit to exit. Do Not Use The X!!!"
print "No blank lines permitted. One space counts as non-empty."
print "Wait for - to type"
while True:
    Recived = s.recv(1024)
    if Recived == "exit ":
        break
    if Recived != "exit ":
        if Recived != "update ":
            if Recived != "about ":
                if Recived != "version ":
                    print("---" + Recived + '\a')
                    Sending = raw_input("-")
                    if Sending == "exit":
                        s.send(Sending + " ")
                        break
                    s.send(Sending + " ")
s.close()                   
