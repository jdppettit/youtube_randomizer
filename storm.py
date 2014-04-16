from flask import *
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from forms import RegistrationForm

import db
from users import User
from secret import HOSTNAME , USERNAME, PASSWORD, DATABASE, SESSION_KEY
from register import makePassword

app = Flask(__name__)
con = db.getConnection(HOSTNAME,USERNAME,PASSWORD,DATABASE)

app.secret_key = SESSION_KEY

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/register', methods=['POST','GET'])
def register(): 	
		form = RegistrationForm(request.form)
		return render_template('register.html', form=form)

@app.route('/register/do', methods=['POST','GET'])
def registerDo():
	if request.method == 'POST':
                form = RegistrationForm(request.form)
                if form.validate():
			user = User(form.username.data, form.password.data, form.email.data)
			db.session.add(user)
			db.session.commit()
			flash('User registered')	
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

