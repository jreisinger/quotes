import os

from api.quotes import app

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = os.environ.get('PORT', 8080)
    app.run(host=host, port=port)
