from flask import render_template
from . import main

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/random', methods=['GET'])
def random():
    return render_template('random.html')
