#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, Flask, make_response
from flask_restful import Resource, Api
from flask_marshmallow import Marshmallow

ma = marshmallow(app)

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Exercise


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

