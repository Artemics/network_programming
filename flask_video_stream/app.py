from flask import Flask, render_template, Response
import cv2 as cv
import random

#// Video Streaming in Web Browsers with OpenCV & Flask
#// https://towardsdatascience.com/video-streaming-in-web-browsers-with-opencv-flask-93a38846fe00

app = Flask(__name__)


camera = cv.VideoCapture(0)

'''
for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
for local webcam use cv2.VideoCapture(0)
'''


def gen_frames():
  while True:
    success, frame = camera.read()
    if not success:
      break
    
    ret, buffer = cv.imencode('.jpg', frame)
    frame = buffer.tobytes()
    
    yield (b'--frame\r\n'
      b'Content-Type: image/jpeg\r\n\r\n' + frame
      + b'\r\n')
      
      
@app.route('/')
def index():
  return render_template('index.html')
  
@app.route('/video_feed')
def video_feed():
  return Response(gen_frames()
    , mimetype='multipart/x-mixed-replace; boundary=frame')
    
    
def gen_randomnum():
  while True:
    yield (b'--sep\r\n'
      + b'Content-Type: text/html\r\n\r\n' + bytes([random.randrange(100)])
      + b'\r\n')

@app.route('/multi_test')
def multi_test():
  return Response(gen_randomnum()
    , mimetype='multipart/mixed; boundary=sep')
   
if __name__ == '__main__':
  app.run(debug=True)
  
    
    
    