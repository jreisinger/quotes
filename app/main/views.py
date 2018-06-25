from flask import render_template
from . import main

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/all', methods=['GET'])
def all():
    return render_template('all.html')
