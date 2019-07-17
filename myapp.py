from flask import Flask,render_template,url_for

app = Flask(__name__)

#@app.route('/')
#def index():
#	return render_template('index.html')

@app.route('/foo/<name>')
def foo(name):
	return render_template('index.html',to=name)


#bootstrap forms
@app.route('/forms')
def forms():
	return render_template('/forms.html')


@app.route('/whereami')
def whereami():
	return 'I am in Ghana,a participant of this years Global Code!!'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
