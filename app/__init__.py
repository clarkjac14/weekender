from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.development')

bootstrap = Bootstrap(app)
from app import routes