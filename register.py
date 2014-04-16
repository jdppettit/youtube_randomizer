import md5

def makePassword(password):
	m = md5.new()
	m.update(password)
	return m.hexdigest()

