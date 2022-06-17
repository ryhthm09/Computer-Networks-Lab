
import socket

ip, port ='localhost' ,5555

s=socket.socket()

s.bind((ip,port))
print(f"Socket created....with {ip}:{port}")
s.listen()
while True:
     conn ,addr=s.accept()
     with conn:
       print(f"Connection established with {addr}")
       conn.send(b"HelloClient")
