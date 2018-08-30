from flask import render_template
from app import app
from .request import get_source

#our views
@app.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    source= get_source()
    print(source)
    return render_template('index.html',sources=source)
