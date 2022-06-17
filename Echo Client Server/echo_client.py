# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 15:01:59 2022

@author: STUDENT
"""

import socket

ip, port = 'localhost',1111

with socket.socket() as c:
    c.connect((ip,port))
    print(f"Connected to {ip}:{port}")
    c.send(b'Hello from client')
    print("data sent")
    print(str(c.recv(1024)))
    
    
