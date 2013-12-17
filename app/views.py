from app import app
from aviation_thing import accidents
from flask import render_template
import json

@app.route('/')
@app.route('/index')
def index():
    data = accidents()
    return render_template ('index.html', title='poop', data=data)