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

Test API

```
# httpie pip package
http --json localhost:5000/api/v1/random
http --json localhost:5000/api/v1/seach/wall
http --json localhost:5000/api/v1/all/
```

Docker

```
# build and run locally
docker build -t quotes:latest .
docker run --name quotes -d -p 5000:5000 quotes:latest
docker logs quotes -f

# push to registry
docker login
docker tag quotes:latest reisinge/quotes:latest
docker push reisinge/quotes:latest

# run from registry (anywhere!)
docker run --name quotes -d -p 5000:5000 reisinge/quotes:latest
```

Resources

* https://github.com/rmotr/flask-api-example
* Flask Web Development, 2nd
