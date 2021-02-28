import itertools
import time
from flask import Flask, Response, redirect, request, url_for, render_template


app = Flask(__name__)

#// https://stackoverflow.com/questions/13386681/streaming-data-with-python-and-flask
#// https://www.html5rocks.com/en/tutorials/eventsource/basics/#disqus_thread
#// "The magical part is that whenever the connection is closed, the browser will automatically reconnect to the source after ~3 seconds."
@app.route('/')
def index():

  #// Accept-* headers indicate the allowed and preferred formats of the response.
  if request.headers.get('accept') == 'text/event-stream':
  
    def events():
      for i, c in enumerate(itertools.cycle('\|/-')):
        yield 'data: %s %d\n\n' % (c, i)
        time.sleep(.1)  #// aritificial delay
    
    return Response(events(), content_type='text/event-stream')
  
  return render_template('index.html')
  #return redirect(url_for('static', filename='index.html'))


def events_global():
  for i, c in enumerate(itertools.cycle('\|/-')):
    yield 'data: %s %d\n\n' % (c, i)
    time.sleep(.1)  #// aritificial delay

@app.route('/test1')
def test1():

  #// Accept-* headers indicate the allowed and preferred formats of the response.
  if request.headers.get('accept') == 'text/event-stream':
  
    return Response(events_global(), content_type='text/event-stream')
  
  return render_template('index.html')
  #return redirect(url_for('static', filename='index.html'))

  
if __name__ == '__main__':
  app.run(debug=True)
  
        
        