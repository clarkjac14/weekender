"""
	Weekender Default Config
"""
import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'pls-dnt-guess-dis'
	DEBUG = False
	TESTING = False