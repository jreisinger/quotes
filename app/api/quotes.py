from flask import Flask, Response
from . import api
import json, random, os
import argparse
import requests
import random
import time
import re
import pickle
import os
import signal
import sys

class Cache:
    def __init__(self, url, cache_file):
        self.url = url
        self.cache = cache_file
        # Create cache file if it does not exist ...
        try:
            file = open(self.cache, 'r')
        except IOError:
            file = open(self.cache, 'w')
    def get_lines(self):
        """ Return list of quotes from a local file. If that is too old
            download them from the Web.
        """
        cache_age = os.path.getmtime(self.cache)
        cache_size = os.path.getsize(self.cache)

        now = time.time()
        day_ago = now - 60*68*24*1

        # cache older than a day or empty
        if cache_age < day_ago or cache_size == 0:
            self._download()

        f = open(self.cache, 'rb')
        self.quotes = pickle.load(f)
        return self.quotes
    def _download(self):
        """ Download quotes from the Web.
        """
        r = requests.get(self.url)
        quotes = ( r.text.split('\n\n') )
        f = open(self.cache, 'wb')
        pickle.dump(quotes, f)

class MyQuote:
    def __init__(self, quotes, length=0):
        # all quotes ...
        self.quotes = []
        if length: # drop quotes longer than length chars
            self.quotes = list(filter(lambda q: len(q) <= int(length), quotes))
        else:
            self.quotes = quotes

        # picked quote(s)
        self.quote = ''
    def all(self):
        #self.quote = '\n\n'.join(self.quotes)
        self.quote = self.quotes
    def pick(self, regex=None):
        """ Pick quotes matching a regex. Or a random quote.
        """
        if regex:
            regex_i = re.compile(regex, re.IGNORECASE)
            quotes = filter( lambda q: re.search(regex_i, q), self.quotes )
            self.quote = list( quotes )
        else:
            try:
                self.quote = random.choice( self.quotes )
            except IndexError: # empty self.quotes
                self.quote = []
    def return_list(self):
        return(self.quote)

quotes = [
    { 'quote': "hello world", 'author': 'Anonymous' },
    { 'quote': "hi world", 'author': 'John Doe' },
]

url = 'https://raw.githubusercontent.com/jreisinger/blog/master/posts/quotes.txt'
cache = Cache(url, '/tmp/myquotes.data')
quotes = MyQuote(cache.get_lines(), length=79)

@api.route('/all/')
def get_all():
    #response = Response( json.dumps(quotes) )
    quotes.all()
    response = Response(
        json.dumps(quotes.return_list()), mimetype="application/json"
    )
    return response

@api.route('/search/<regex>')
def search(regex):
    quotes.pick(regex)
    response = Response(
        json.dumps(quotes.return_list()), mimetype="application/json"
    )
    return response

@api.route('/random')
def get_random():
    quotes.pick()
    response = Response(
        json.dumps(quotes.return_list()), mimetype="application/json"
    )
    return response
