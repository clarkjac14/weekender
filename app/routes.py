from flask import Flask, render_template, request, flash, redirect
from app import app
from app.forms.weekend import TimeForm
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