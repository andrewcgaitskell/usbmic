import socket

HOST = '192.168.1.8'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
hellomessage = 'Hello, world'
hello_as_bytes = str.encode(hellomessage)
s.sendall(hello_as_bytes)
data = s.recv(1024)
s.close()
print('Received', repr(data))
