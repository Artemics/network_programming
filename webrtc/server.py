from flask import Flask, url_for, render_template, redirect


app = Flask(__name__, static_folder='static')


@app.route('/')
def root():
  return redirect(url_for('index'))

@app.route('/index')
def index():
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)
