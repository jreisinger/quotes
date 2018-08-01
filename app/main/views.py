from flask import render_template
from . import main

# NOTE: @main.route is used instead of @app.route because we are in a blueprint
@main.route('/', methods=['GET'])
def index():
    return render_template('random.html')

@main.route('/all', methods=['GET'])
def all():
    return render_template('all.html')

@main.route('/kids', methods=['GET'])
def kids():
    return render_template('kids.html')

@main.route('/api', methods=['GET'])
def api():
    return render_template('api.html')
