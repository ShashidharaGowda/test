from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)
#dbHandler.insertUser(username, password)
#users = dbHandler.retrieveUsers()
@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method=='POST':
		data = request.get_json()
		print(data)
		return "Success"
	else:
		return "Regester"



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')