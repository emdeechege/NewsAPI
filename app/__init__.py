from flask import Flask
from .config import DevConfig

#app initialization
app= Flask(__name__)

#set up configuration
app.config.from_object(DevConfig)



from app import views
