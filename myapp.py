from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello Christian'

@app.route('/whereami')
def whereami():
	return 'I am in Ghana,a participant of this years Global Code!!'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')







