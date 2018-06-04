from flask import Flask, Response
from . import api
import json

quotes = [
    { 'quote': "hello world", 'author': 'Anonymous' },
    { 'quote': "hi world", 'author': 'John Doe' },
]

@api.route('/quotes/')
def get_quotes():
    response = Response( json.dumps(quotes) )
    return response
