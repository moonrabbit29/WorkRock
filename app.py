from flask import Flask,render_template,request,jsonify,send_file
from flask_cors import CORS,cross_origin
from datetime import datetime
import os
from fuzzy import Fuzzy


app = Flask(__name__, template_folder='public/templates')
cors = CORS(app)

app.config['url'] = ''

@app.route("/public/<path:filename>")
def public(filename):
   basedir=os.path.dirname(os.path.abspath(__file__))
   filename = os.path.join(basedir,"public/"+filename)
   if(os.path.isfile(filename)) : return send_file(filename)
   else : return 

@app.route('/',methods=['GET','POST'])
def index():
   if request.method == 'GET' : 
      return render_template("index.html")
   if request.method == 'POST':
      print(request.body);

@app.route('/getAcTemp',methods=['POST'])
@cross_origin()
def getAcTemp():
   data = request.get_json()
   Fuzzy.valueIinitialization(data['insideTemp'],data['outsideTemp'],data['people'])
   bestTemp = Fuzzy.inferensi()
   return jsonify({'OptimalTemperature': bestTemp}),200


app.jinja_env.globals.update(config=app.config)

