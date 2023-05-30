from socket import *

s = socket(AF_INET,SOCK_STREAM)

host = "127.0.0.1"
port = 7002

s.connect((host, port))

while True:
    text_in = input("client : ")
    s.send(text_in.encode('utf=8'))
    if text_in == 'Q':
        break

    rece_data = s.recv(2048)
    if rece_data.decode('utf=8') == 'Q':
        break
    print ("server: " , rece_data.decode('utf=8'))


s.close()
