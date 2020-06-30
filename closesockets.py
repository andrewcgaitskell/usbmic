import socket
import select

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 50007))
serversocket.close()
