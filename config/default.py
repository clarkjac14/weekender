"""
	Weekender Default Config
"""
import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'pls-dnt-guess-dis'
	WTF_CSRF_SECRET_KEY="a csrf secret key"
	DEBUG = False
	TESTING = False