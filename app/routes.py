from flask import render_template
from app import app
from app.forms import LoginForm
import datetime, os

@app.route('/')
@app.route('/index')
def index():
	date = datetime.datetime.today().strftime('%A, %B %-d')
	return render_template('index.html', Today = date)


@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)
	
"""
if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
"""