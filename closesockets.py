import socket
import select

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  serversocket.bind(('', 50007))
except:
  pass
serversocket.close()
