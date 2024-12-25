from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
  return "Alive"

def run():
  app.run(port=10000)

def keep_alive():  
  t1 = Thread(target=run)
  t1.start()

keep_alive()
