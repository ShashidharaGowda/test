import sqlite3 as sql
def insertUser(username,password):
    con = sql.connect("test.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()
def retrieveUsers(user,pas):
	con = sql.connect("test.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users where username='{}' and password='{}'".format(user,pas))
#	cur.execute(".tables;")
	users = cur.fetchall()
	con.close()
	return bool(len(users))
print(retrieveUsers("shashi","shashi12345"))