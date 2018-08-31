from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

# #initialize Bootstrap
# Bootstrap(app)

# Initializing flask extensions
bootstrap.init_app(app)

return app
