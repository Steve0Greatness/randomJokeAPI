from flask import Flask, send_file
import random

app = Flask(__name__)

# list of jokes
with open('jokes.txt') as file:
	jokes = file.read().split('\n')

@app.route('/')
def home():
  return { 'joke': random.choice(jokes) }

@app.route('/txt')
def plain():
  return random.choice(jokes)

@app.route('/docs')
def docs():
  return send_file('docs.html')

def run():
  app.run(host='0.0.0.0',port=8080)

if __name__ == "__main__":
	run()