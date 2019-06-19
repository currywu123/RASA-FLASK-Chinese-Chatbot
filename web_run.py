from flask import Flask 
from flask import render_template, jsonify
from flask import request
from flask import redirect, url_for

from flask_wtf import CSRFProtect
from web_forms import RequestForm 

from web_models import handle_saying

app = Flask(__name__)
app.config.from_pyfile('web_config.py')

dialog = []

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/chat', methods = ['POST'])
def chat():
	try:
		user_message = request.form['text']
		response_text = handle_saying(user_message)
		return jsonify({'status':'success', 'response':response_text})
	except Exception as e:
		print(e)
		return jsonify({'status':'success', 'response':'抱歉出错了'})

if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 8666, debug = True)

