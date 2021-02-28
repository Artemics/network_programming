import socket
import sys

def udp():
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hello UDP', (HOST, PORT))
  
def tcpIp():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(BufferSize)
    print(repr(data))
    s.sendall(b'hello TCP/IP')
    data = s.recv(BufferSize)
    print(repr(data))

    
if __name__ == '__main__':

  HOST = '127.0.0.1'
  PORT = 50007
  BufferSize = 1024
  
  if len(sys.argv) <= 1:
    tcpIp()
  else:
    mode = sys.argv[1]
    if mode == 'u':
      udp()
    elif mode == 't':
      tcpIp()

