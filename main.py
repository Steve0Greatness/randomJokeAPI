from flask import Flask, send_file
from random import choice

app = Flask(__name__)

# list of jokes
with open('jokes.txt') as f:
	jokes = f.read().split('\n')

@app.route('/')
def json():
  return { 'joke': choice(jokes) }

@app.route('/txt')
def text():
  return choice(jokes)

@app.route('/docs')
def docs():
  return send_file('docs.html')

if __name__ == "__main__":
	app.run('0.0.0.0')