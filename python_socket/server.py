import socket
import sys

#// References
#// pythonでsocket通信を勉強しよう
#// https://qiita.com/__init__/items/5c89fa5b37b8c5ed32a4
#// 


def udp():

  print("udp")

  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("udp: s.bind successful")
    while True:
      data, addr = s.recvfrom(BufferSize)
      print('data: {}, addr: {}'.format(data, addr))



def tcpIp():

  print("tcpip")
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    #// Allowing only one connection?
    s.listen(1)
    print("tcpIp: s.bind&listen successful")

    while True:
      conn, addr = s.accept()
      conn.send(bytes('Welcome to the server!', 'utf-8'))
      with conn:
        print('Connected by', addr)
        while True:
          data = conn.recv(BufferSize)
          if not data:
            break
          print('data: {}, addr: {}'.format(data, addr))
          
          conn.sendall(b'Received: ' + data)
        #conn.close()

    #// repr() returns a string that holds a printable representation of an object.
    
    
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

