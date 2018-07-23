from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, RadioField
from wtforms.validators import DataRequired

class TimeForm(FlaskForm):
	name = StringField("Your name", validators=[DataRequired()])
	
	friday = RadioField("Friday", 
		choices=[('y','yes'), ('n','no')], 
		default = 'y', 
		validators=[DataRequired()])
	
	saturday = RadioField("Saturday", 
		choices=[('y','yes'), ('n','no')], 
		default = 'y',
		validators=[DataRequired()])
	
	sunday = RadioField("Sunday", 
		choices=[('y','yes'), ('n','no')], 
		default = 'y',
		validators=[DataRequired()])
	
	submit = SubmitField('Submit')