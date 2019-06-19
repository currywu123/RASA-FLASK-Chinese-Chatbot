from flask import Flask 
from flask import render_template
from flask import request
from flask import redirect, url_for

from flask_wtf import CSRFProtect
from web_forms import RequestForm 

from web_models import handle_saying


app = Flask(__name__)
app.config.from_pyfile('web_config.py')

CSRFProtect(app)

dialog = []

@app.route('/')
@app.route('/request/', methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		form = RequestForm()
		return render_template('request.html', form = form)
	else:
		form = RequestForm(request.form)
		if form.validate():
			print('输入成功，正在处理')
			saying = form.saying.data
			print('获取输入：{}'.format(saying))
			dialog.append(saying)

			bot_response = handle_saying(saying)
			print('处理结果：{}'.format(bot_response))
			dialog.append(bot_response)

			info = {'contents': dialog}

			form.saying.data = ""
			return render_template('request.html', form = form, **info)
		else:
			info = form.errors
			form = RequestForm()
			return render_template('request.html', form = form, **info)

print(app.url_map)
if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 8666, debug = True)


