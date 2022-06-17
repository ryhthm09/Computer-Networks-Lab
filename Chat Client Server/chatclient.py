import socket

ip ,port ='localhost',5555

with socket.socket() as c:
    c.connect((ip,port))
    print(f"connnected with server {ip}:{port}")

    while True:
        message=input("client: ")
        c.send(message.encode('utf-8'))
        if(message.lower().strip()=='bye'):
            break
        received=c.recv(1024).decode('utf-8')
        print(f'Server: {received}')
        
        
            
