"""
	Weekender Config
"""
import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'pls-dnt-guess-dis'
	DEBUG = True
	TESTING = True

class DevelopmentConfig(Config):
	DEBUG = True
	Testing = True