import socket               # Import socket module

s = socket.socket()         # Create a socket object
s.bind(( '', 4500))         # Bind to the port
s.listen(5)                 # Now wait for client connection.
print "Server Main 1 Conversation"
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   while True:
      Recived = c.recv(1024)
      if Recived == "exit ":
         print "Client Exiting"
         print ""
         break
      print "---" + Recived + '\a'
      Sending = raw_input("-")
      c.send(Sending + " ")
      if Sending == "exit":
         print "Server Exiting"
         print ""
         break
   c.close()
