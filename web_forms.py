from flask_wtf import FlaskForm
from wtforms import Form, StringField
from wtforms.validators import InputRequired

class RequestForm(FlaskForm):
	saying = StringField(
		label = '你想说的话', 
		validators =  [InputRequired('话语不能为空')])