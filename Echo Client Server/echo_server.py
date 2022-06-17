# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 14:48:26 2022

@author: STUDENT
"""

import socket

ip, port = 'localhost',1111

with socket.socket() as s:
    s.bind((ip,port))
    print(f"socket created at{ip}:{port}")
    s.listen()
    
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        if data:
            print(f"Server received {data.decode('UTF-8')}")
            conn.send(bytes(str(data)+" (returned from server)", 'utf-8'))
        else:
            conn.send(b'No data Received')
    

