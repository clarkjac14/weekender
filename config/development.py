"""
	development.py
	Activates DEBUG and Testing
"""
from config.default import Config

class Config(Config):
	DEBUG = True
	Testing = True
	print("****This app is running in development mode!****\n"+
	"****Please edit the configuration before deploying to production!****")