from flask import Flask, render_template, request
from threading import Thread
from replit import db

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
  if request.method == "POST":
    pass

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()