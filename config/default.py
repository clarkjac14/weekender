"""
	Weekender Default Config
"""
import os
appdir = os.path.abspath(os.path.dirname(__file__))[:-6] + 'app/'

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'pls-dnt-guess-dis'
	WTF_CSRF_SECRET_KEY='a csrf secret key'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(appdir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
	
	#Settings
	
	DEBUG = False
	TESTING = False