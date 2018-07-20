from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, RadioField
from wtforms.validators import DataRequired

class TimeForm(FlaskForm):
	name = StringField("Your name", validators=[DataRequired()])
	friday = RadioField("Friday", choices=[('value','yes'), ('value_two','no')], validators=[DataRequired()])
	saturday = RadioField("Saturday", choices=[('value','yes'), ('value_two','no')],validators=[DataRequired()])
	sunday = RadioField("Sunday", choices=[('value','yes'), ('value_two','no')],validators=[DataRequired()])
	submit = SubmitField('Submit')