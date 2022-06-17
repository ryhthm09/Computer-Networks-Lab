
import time
import socket

ip ,port ='localhost',5555

with socket.socket() as s:
    s.bind((ip,port))
    print(f"Socket created with {ip}:{port}")
    s.listen()

    while True:
        conn , addr =s.accept()
        data= conn.recv(1024).decode('utf-8')

        if data=='get time':
            conn.send(bytes(time.ctime(),"utf-8"))
            print("time sent")
        else:
            print("no data received")
