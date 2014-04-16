from wtforms import Form, BooleanField, TextField, PasswordField, validators

class RegistrationForm(Form):
	username = TextField('Username', [validators.Length(min=5, max=25)])
	email = TextField('Email Address', [validators.Length(max=50)])
	password = PasswordField('Password', [
		validators.Required(),
		validators.EqualTo('confirm', message='Passwords must match')
	])
	confirm = PasswordField('Repeat Password')
