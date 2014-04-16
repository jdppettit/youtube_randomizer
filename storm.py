from flask import *
from flask.ext.sqlalchemy import SQLAlchemy
from forms import RegistrationForm

import db
from register import makePassword


app = Flask(__name__)
con = db.getConnection('mysql.home','stormdevuser','stormdevpassword','storm_dev')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/register', methods=['POST','GET'])
def register(): 	
	if request.method == 'POST':
	        form = RegistrationForm(request.form)
		if form.validate():
			hashedPassword = ""
			username = ""
			email = ""
			hashedPassword = hashedPassword.join((makePassword(form.password.data)))
			username = username.join(form.username.data)
			email = email.join(form.email.data)
			cur = con.cursor()
			cur.execute("INSERT INTO users(username,email,password) VALUES('%s','%s','%s');" % (username, email, hashedPassword))
			return redirect(url_for('login')) 
		else:
			return render_template('register.html',error="Please fill out the entire form",form=form)
	else:
		print "Request was not a POST"
		form = RegistrationForm(request.form)
		return render_template('register.html', form=form)

@app.route('/account')
def account():
	return render_template('account.html')

@app.route('/playlist')
def playlist():
	return render_template('playlist.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)

