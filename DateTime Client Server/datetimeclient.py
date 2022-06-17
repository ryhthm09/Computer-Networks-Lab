import socket

ip ,port ='localhost',5555

with socket.socket() as c:
    c.connect((ip,port))
    c.send(b'get time')
    print(f"the server time is {c.recv(1024).decode('utf-8')}")
