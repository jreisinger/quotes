# https://github.com/rmotr/flask-api-example

from flask import Flask, Response
import json

app = Flask(__name__)

quotes = [
    { 'quote': "hello world", 'author': 'Anonymous' },
    { 'quote': "hi world", 'author': 'John Doe' },
]

@app.route('/quotes/')
def get_quotes():
    response = Response( json.dumps(quotes) )
    return response
