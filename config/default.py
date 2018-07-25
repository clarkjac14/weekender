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
	
	print(appdir)
	
	#Settings
	
	DEBUG = False
	TESTING = False