from flask import render_template
from app import app

#our views
@app.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    message= "test for"
    return render_template('index.html',message=message)
