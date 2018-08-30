from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#app initialization
app= Flask(__name__,instance_relative_config = True)

#set up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initialize Bootstrap
boostrap= Bootstrap(app)


from app import views
