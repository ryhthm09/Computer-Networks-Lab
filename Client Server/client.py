import socket

ip ,port = 'localhost',5555

with socket.socket() as c:
    c.connect((ip,port))
    print(f"Connected with server {ip}:{port}")
    print(f" received data : {c.recv(1024).decode('utf-8')}")
