from socket import *                                    # first of all import the socket library
s = socket(AF_INET,SOCK_STREAM)            # next create a socket object
print ("Socket successfully created")            # socket successfully created
 # reserve a port on your computer in our case it is 40674 but it can be anything
host ='127.0.0.1'
port = 40674
 # Next bind to the host (IP address) and port number. 
s.bind((host, port))                                         # the arguments in bind is in tuple format
print ("socket binded to  ",port)                      # socket binded to 40674
s.listen(5)                                                             # put the socket into listening mode
print ("socket is listening")                               # socket is listening
 # a forever loop until we interrupt it or an error occurs
while True:
 c, addr= s.accept()                                     # Establish connection with client.
 print ('Get connection from', addr)                      #Get connection from (‘127.0.0.1‘, 55182)
 c.send(b'Thankyou for connecting')          # send a message to the client.
 c.close()        