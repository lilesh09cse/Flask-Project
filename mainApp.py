
from flask import Flask, render_template,request,session
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/aboutus')
def about():
    return render_template('aboutus.html')

@app.route('/contactus')
def contact():
    return render_template('contactus.html')

@app.route('/about')
def aboutnew():
    return render_template('about.html')

@app.route('/contact')
def contactnew():
    return render_template('contact.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/myskill')
def skill():
    return render_template('skill.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/saveResult',methods=['POST','GET'])
def save():
    if request.method == "POST":
        pageData = request.form     #.form is property that will return the submitted data in page
        session['username']=request.form['usertxt']
        #in aboove line we created session variable it is username
        # it can be anything 
        #in session variable we are fetching the data from usertxt (name attributr) txtfield from 
        #signup.html
        #return pageData
        return render_template('success.html',myoutput=pageData)
    #return 'Sahi hai! Chal raha hai'

app.secret_key="anything here"

@app.route('/admin')
def admin():
    return f"current user logged in {session['username']}"

# Handler for signout
@app.route('/signout')
def signout():
    session.pop('username',None)
    #return "user is signed out"
    return render_template('home.html')


app.run(debug = True)