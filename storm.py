from flask import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/register')
def register(): 	
	return render_template('register.html')

@app.route('/account')
def account():
	return render_template('account.html')

@app.route('/playlist')
def playlist():
	return render_template('playlist.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)

