from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Log In')
	
class AvailabilityForm(FlaskForm):
	name = TextField("Your name", validators=[DataRequired()])
	friday = DateTimeField("Friday", validators=[DataRequired()])
	saturday = DateTimeField("Saturday", validators=[DataRequired()])
	sunday = DateTimeField("Sunday", validators=[DataRequired()])
	submit = SubmitField('Submit')