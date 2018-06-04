from flask import Flask, Response
from . import api
import json
import random

quotes = [
    { 'quote': "hello world", 'author': 'Anonymous' },
    { 'quote': "hi world", 'author': 'John Doe' },
]

@api.route('/all/')
def get_all():
    response = Response( json.dumps(quotes) )
    return response

@api.route('/random')
def get_random():
    response = Response( json.dumps( random.choice(quotes) ))
    return response
