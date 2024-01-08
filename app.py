from flask import Flask
from threading import Thread
import requests
import time

app = Flask('')

# Define the URL you want to ping


@app.route('/')
def home():
  return "Hello. I am alive!"


def run():
  app.run(host='0.0.0.0', port=8080)



def keep_alive():
  t1 = Thread(target=run)
  t1.start()
  


if __name__ == '__main__':
  keep_alive()
