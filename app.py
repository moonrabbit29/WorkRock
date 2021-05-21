from flask import Flask,render_template,request,redirect
from datetime import datetime


app = Flask(__name__, template_folder='public/templates')

@app.route('/',methods=['GET'])
def index():
   if request.method == 'GET' : 
      return render_template("index.html")
