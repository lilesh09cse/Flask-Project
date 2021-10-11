from flask import Flask
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)
# app is an object which is representing the flask app.

# __name__ is a builtin object which contains the file name i.e.
# hello.py or __main__ so basically it means that the 
# name of application is set as hello

# / means http://localhost:5000

# functions are called via endpoints e.g.
# @app.route('/showmeindia') showmeindia is endpoint
# so in URL http://localhost:5000/showmeindia

#@app.route() is a method which represents the
#path to access/call the function below

@app.route("/") 

def index():
    return "india"



@app.route("/aboutme") 

def myintro():
    return "I love "



# how to define route

@app.route("/article/<int:articleNo>")
def getArticle(articleNo):
    return f"returns Article {articleNo}"

@app.route("/patient/<float:patientId>")
def getPatientId(patientId):
    return f"Patient Id: {patientId}"

@app.route("/employee/<ename>")
def start_employee(ename):
    return f"Hello Employee {ename}"

@app.route("/manager/<mname>")
def start_manager(mname):
    return f"Hello Manager {mname}"

@app.route("/checkrole/<role>")
def checkRole(role):
    if role == 'manager':
        return redirect(url_for('start_manager',mname = 'Default Manager'))
    else:
        return redirect(url_for('start_employee',ename = 'Default Employee'))
#from flask.helpers import url_for
#from werkzeug.utils import redirect

@app.route("/fruits/<fname>")
def showFruits(fname):
    return f"Showing Fruits {fname}"

@app.route("/vegetables/<vname>")
def showVegetables(vname):
    return f"Showing Vegetables {vname}"


@app.route("/product/<ptype>")
def fruitType(ptype):
    if ptype == 'fruit':
        return redirect(url_for('showFruits',fname = 'Default fruit'))
    elif ptype == 'vegetable':
        return redirect(url_for('showVegetables',vname = 'Default vegetable'))
    else:
        return "Invalid Product Type!!!! Try Again"
app.run(debug=True)