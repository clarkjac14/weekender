from flask import Flask, render_template, request, flash, redirect
from app import app
from app.forms.weekend import TimeForm
from app.models import Timeslot as table
from app import db
import datetime, os

@app.route('/', methods = ['GET','POST'])
def index():
	form = TimeForm()
	date = datetime.datetime.today().strftime('%A, %B %-d')
	
	if form.validate_on_submit():
		flash('Thank you for submitting, {}.'.format(form.name.data))
		return redirect('/')
	else:
		flash('Something went wrong!')
	return render_template('index.html', Today=date, form=form)
	
@app.route('/dbtest')
def dbtest():
	result = ''
	for row in table.query.all():
		result = result + str(row)[1:-1] + '<hr>'
	return result

@app.route('/name/<username>')
def name(username):
	name = Timeslot.query.filter_by(name=username).all()
	return str(name)