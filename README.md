# quotes

Learning how to create an API in Flask.

Develop

* enable [venv](https://github.com/jreisinger/blog/blob/master/posts/python-venv.md)
* run

```
export FLASK_DEBUG=1
export FLASK_APP=quotes.py
flask run
```

* work hard

Test

```
# httpie pip package
http --json localhost:5000/api/v1/all/
```


Resources

* https://github.com/rmotr/flask-api-example
* Flask Web Development, 2nd
