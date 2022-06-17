import socket

ip, port= 'localhost',5555

with socket.socket() as s:
  s.bind((ip,port))
  print(f"The connection is established {ip}:{port}")
  s.listen()

  while True:
      conn ,addr=s.accept()
      received = " "
      while(received.lower()!='bye'):
          received=conn.recv(1024).decode('utf-8')
          print(f'Client : {received}')
          if received.lower()=='bye':
              message='bye'
              print("Server :",message)
              conn.close()
              break
          else:
              message=input("server :")
              conn.send(message.encode('utf-8'))
      
