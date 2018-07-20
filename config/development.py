"""
	development.py
	Activates DEBUG and Testing
"""
from config.default import Config

class DevelopmentConfig(Config):
	DEBUG = True
	Testing = True
	print("Development mode activated!")