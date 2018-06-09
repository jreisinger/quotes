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

* work hard :-)

Test

```
# httpie pip package
http --json localhost:5000/api/v1/random
http --json localhost:5000/api/v1/seach/wall
http --json localhost:5000/api/v1/all/
```

Docker

```
docker build -t quotes:latest .
docker run --name quotes -d -p 8000:5000 quotes:latest
dokcker logs quotes -f
```

Resources

* https://github.com/rmotr/flask-api-example
* Flask Web Development, 2nd
