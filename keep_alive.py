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
    fname = request.form["first"]
    lname = request.form["last"]
    email = request.form["email"]
    if "database" in db.keys():
      database = db["database"]
      data = [fname, lname, email]
      database.append(data)
      db["database"] = database
    else:
      database = []
      data = [[fname, lname, email]]
      db["database"] = data
    print("new profile added {}, {}".format(fname, lname))
    return render_template("success.html")
def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()