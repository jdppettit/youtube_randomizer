import MySQLdb as mdb 

def getConnection(ip, username, password, db):
	try:
		con = mdb.connect(ip,username,password,db)
	except _mysql.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
	
	return con


