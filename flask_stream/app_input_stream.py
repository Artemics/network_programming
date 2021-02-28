from flask import Flask, Response, redirect, request, url_for, render_template
import numpy as np
import socket

import itertools
import time
import sys

#// References
#// pythonでsocket通信を勉強しよう
#// https://qiita.com/__init__/items/5c89fa5b37b8c5ed32a4
#// 

app = Flask(__name__)

@app.route('/')
def udp():
  
  HOST = '127.0.0.1'
  PORT = 50007
  BufferSize = 1024
  
  if request.headers.get('accept') == 'text/event-stream':
  
    def udpInput():
    
      with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

        s.bind((HOST, PORT))
        print("udp: s.bind successful")

        byteData, addr = s.recvfrom(BufferSize)
        #// '<f4' specifies little-endian 32-bit float.
        data = np.frombuffer(byteData, np.dtype('<f4'))        
        print('data: {}, addr: {}'.format(data, addr))
        
        yield 'data: %s %s\n\n' % (data, byteData)
        #yield 'data: %s %s\n\n' % (float(data.decode()), data)
  
    return Response(udpInput(), content_type='text/event-stream')
    
  return render_template('index.html')


#// https://www.html5rocks.com/en/tutorials/eventsource/basics/#disqus_thread
#// "The magical part is that whenever the connection is closed, the browser will automatically reconnect to the source after ~3 seconds."
@app.route('/simple_stream')
def simple_stream():

  #// Accept-* headers indicate the allowed and preferred formats of the response.
  if request.headers.get('accept') == 'text/event-stream':
  
    def events():
      for i, c in enumerate(itertools.cycle('\|/-')):
        yield 'data: %s %d\n\n' % (c, i)
        time.sleep(.1)  #// aritificial delay
    
    print('if request')
    return Response(events(), content_type='text/event-stream')
  
  print('index')
  return render_template('index.html')
  #return redirect(url_for('static', filename='index.html'))
  
    

def udp_():

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

  # HOST = '127.0.0.1'
  # PORT = 50007
  # BufferSize = 1024
  
  app.run(debug=True)
  

