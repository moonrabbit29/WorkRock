from flask import Flask,render_template,request,redirect,send_file
from datetime import datetime
import os


app = Flask(__name__, template_folder='public/templates')

@app.route("/public/<path:filename>")
def public(filename):
   basedir=os.path.dirname(os.path.abspath(__file__))
   filename = os.path.join(basedir,"public/"+filename)
   if(os.path.isfile(filename)) : print("hello")
   return send_file(filename)

@app.route('/',methods=['GET','POST'])
def index():
   if request.method == 'GET' : 
      return render_template("index.html")
   if request.method == 'POST':
      print(request.body);

