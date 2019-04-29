from os import environ

from app import app

HOST = environ.get('FLASK_HOST', '127.0.0.1')
PORT = int(environ.get('FLASK_PORT', 5000))

app.run(host=HOST, port=PORT)
