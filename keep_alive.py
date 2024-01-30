from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
  return "Server Alive!"

def run():
  app.run(debug=True, port=5000)


def keep_alive():
  t = Thread(target=run)
  t.start()
