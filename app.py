
from flask import Flask, url_for, render_template, redirect, session,request

from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy




#from flask_ngrok import run_with_ngrok

                    



"""
login-if user found, success
else asks to register"""



# from flask_session import Session

import faceLoginApp
import facecode

app = Flask(__name__)
socketio = SocketIO(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
#run_with_ngrok(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)
recognizer = faceLoginApp.UserLogin
captureface=facecode.FaceCapture



# class User(db.Model):
# 	""" Create user table"""
# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String(80), unique=True)
# 	password = db.Column(db.String(80))

# 	def __init__(self, username, password):
# 		self.username = username

# 		self.password = password

class User(db.Model):
	""" Create user table"""
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)

	def __init__(self, username):
		self.username = username
        


@app.route('/', methods=['GET', 'POST'])
def home():
	""" Session control"""
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		if request.method == 'POST':

			return render_template('index.html') 
		return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():        
        ret = recognizer.captureAndCompare('aru')
        
        if ret==1:
            return("Sucessfully logged in. Welcome to MEFY")
        else:
            
            #return render_template('register.html')
            return redirect(url_for('register'))



@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['username']
        ret=captureface.FuncCap(name)
        if ret==1:
            return redirect(url_for('home'))
        else:
        
                return render_template('index.html')
    return render_template('register.html')


# @app.route('/capture/')

# def capture():
#     getname= User()
#     name=getname.username

#     ret= captureface.FuncCap(name)
#     print(ret)
#     return render_template('index.html')

# @app.route('/register/', methods = ["GET","POST"])
# def register():############or get usernumber from user if h=getting name doesnt work well
#     global user_name

#     if request.method == "POST":
#         user_name = request.form["answer"]
#         # if user_name [-1] == data[answer_number]["answer"]:
#         #     answer_number += 1
#         #     user_correct += 1
#         # else:
#         #     user_wrong += 1
#         print (user_name)
#         return render_template("register.html", user_name=user_name)






                         
            
  

# @app.route('/register/', methods=['GET', 'POST'])
# def register():
#     	if request.method == 'POST':

    
#             name = request.form['username']

    
#             returnval=captureface.FuncCap(name)
#             if returnval==True:
#                 return redirect(url_for('home'))
#             elif returnval==False:
#                 return ("Failed user registration. Please try again")
        
    
    
    
# 	if request.method == 'POST':
# 		new_user = User(username=request.form['username'], password=request.form['password'])
# 		db.session.add(new_user)
# 		db.session.commit()
# 		return render_template('login.html')
# 	return render_template('register.html')

@app.route("/logout")
def logout():
	"""Logout Form"""
	session['logged_in'] = False
	return redirect(url_for('home'))


if __name__ == '__main__':
    db.create_all()
    app.run()
	#app.debug = True
	
